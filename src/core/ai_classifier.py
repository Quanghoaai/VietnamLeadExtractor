import pandas as pd
from typing import List
from transformers import pipeline
from src.utils.logger import get_logger

logger = get_logger(__name__)

class LeadClassifier:
    """
    Lớp áp dụng mô hình phân loại Zero-shot Classification (Hugging Face / PyTorch)
    Đánh giá dựa vào Tên (Chức năng), Đánh giá (Rating), và Số lượng đánh giá (Review Count).
    Mô hình tự sinh labels cho người dùng chắt lọc ra 'Leads chất lượng cao' vs 'Leads kém' 
    mà không cần pre-train riêng biệt trên tập data B2B nào cả.
    """
    
    def __init__(self):
        """
        Khởi tạo Pipeline NLP Zero-shot mô hình lớn để suy luận ngữ nghĩa B2B.
        Đã chuyển qua bản AI Rút Gọn (MiniLM) cực nhẹ ~100MB, tải chỉ mất 5s thay vì 1.6GB.
        """
        logger.info(" Đang load & Cache model AI local từ Hugging Face. (Bản Mini siêu nhẹ ~110MB).")
        try:
            # Sử dụng bản mDeBERTa/MiniLM đa ngôn ngữ giúp tốc độ siêu nhanh (vài chục MB / load vài giây)
            # Thay vì facebook/bart-large-mnli (1.6 GB) làm nghẽn máy tính.
            self.classifier = pipeline("zero-shot-classification", model="MoritzLaurer/Multilingual-MiniLMv2-L6-mnli-xnli")
            # Danh mục đích: Điểm chất lượng B2B Leads.
            self.candidate_labels = ["chất lượng cao", "chất lượng trung bình", "chất lượng thấp"]
        except Exception as e:
            logger.error(f" Failure - Mô hình load thất bại (Thiếu RAM hoặc mất mạng): {e}")
            self.classifier = None
            
    def classify_leads(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Hàm phân tích hàng loạt cho khung dữ liệu đầu vào. Gán điểm bằng cách loop từng Lead.
        
        Args:
            df (pd.DataFrame): Input DataFrame đã được qua Processor dọn sạch.
            
        Returns:
            pd.DataFrame: Output dataframe kèm cột bonus 'lead_quality'.
        """
        if self.classifier is None:
            logger.warning(" AI Model Pipeline chập chờn hoặc chưa khởi tạo. Bỏ qua phase gán nhãn AI Score.")
            df['lead_quality'] = "Không thể phân loại"
            return df
            
        if df.empty:
            return df
            
        logger.info(" Bắt đầu vòng lặp suy luận AI (Inference pass) chấm điểm cho các doanh nghiệp thu được...")
        
        qualities = []
        for idx, row in df.iterrows():
            title = row.get('title', '')
            rating = row.get('rating', '')
            reviews = row.get('reviewCount', 0)
            
            # Tiền xử lý ép kiểu, nếu rating rỗng (không ai rate trên map) -> cho là 0.0
            numeric_rating = 0.0
            if is_number(rating):
                numeric_rating = float(rating)
                
            numeric_reviews = 0
            if is_number(reviews):
                numeric_reviews = int(reviews)
            
            # Heuristic Rule: Nếu số sao < 3 mà lại có khá review (chứng tỏ bị tẩy chay nhiều) -> ép rule thấp cho tiết kiệm compute AI.
            if numeric_rating > 0 and numeric_rating < 3.0 and numeric_reviews >= 3:
                qualities.append("chất lượng thấp")
                continue
            
            # Nếu ko có rating/review nào, cho mặc định trung bình (doanh nghiệp mới lên sàn/map).
            if numeric_reviews == 0:
                qualities.append("chất lượng trung bình")
                continue
                
            # Đóng gói Prompt text cực nhỏ gọn mô tả bản thể cho AI pipeline đưa ra dự đoán.
            text_context = f"Doanh nghiệp: {title}. Đánh giá: {numeric_rating} sao với {numeric_reviews} lượt bình luận."
            
            try:
                # API predict Pipeline
                result = self.classifier(text_context, candidate_labels=self.candidate_labels)
                # Vì array trả ra luôn sort descending percent match -> chọn index [0]
                best_label = result['labels'][0]
                
                # Biến tấu Label Anh / Việt theo chuẩn cho đẹp
                label_mapper = {
                    "chất lượng cao": "High",
                    "chất lượng trung bình": "Medium",
                    "chất lượng thấp": "Low"
                }
                
                final_val = label_mapper.get(best_label, "Medium")
                qualities.append(final_val)
                
            except Exception as e:
                logger.debug(f" Lỗi suy luận dòng ID {idx}: {e}")
                qualities.append("Medium")
                
        df['lead_quality'] = qualities
        logger.info(" Trí tuệ nhân tạo (Hugging Face) hoàn tất việc gán nhãn điểm chất lượng B2B Leads.")
        return df

def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
