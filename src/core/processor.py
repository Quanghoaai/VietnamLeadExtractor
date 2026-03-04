import pandas as pd
from typing import List, Dict, Any
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataProcessor:
    """
    Class tiếp nhận mảng đối tượng thô (Raw) từ bộ Scraper trả về,
    chuẩn hóa, làm sạch (Cleaning), bóc tách nội dung (Parsing) 
    và khử trùng lặp (Deduplicate) sử dụng thư viện mạnh mẽ là Pandas.
    """
    
    def process(self, raw_data: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Phương thức chính. Chuyển đổi List[Dictionary] mảng raw thành DataFrame vệ sinh gọn gàng.
        
        Args:
            raw_data (List[Dict[str, Any]]): Khối lượng đối tượng JSON thô gom về từ Scraper/Google.
            
        Returns:
            pd.DataFrame: Khối DataFrame (bảng) đã xử lý xong, có thể đưa vô Database hoặc ML Model.
        """
        if not raw_data:
            logger.warning(" Tham số List dữ liệu raw đầu vào trống. Không có gì để chạy DataProcessor.")
            return pd.DataFrame()
            
        df = pd.DataFrame(raw_data)
        logger.info(f" Đã map List vào DataFrame gốc Pandas. Khối Data chứa {len(df)} records đang nằm trên RAM memory.")
        
        # Select những fields thiết thực nhất dành cho phòng Sales/Marketing
        columns_to_keep = [
            "title", "address", "phone", "website", 
            "rating", "reviewsCount", "categoryName", "location"
        ]
        
        # Chỉ retain những cột thực sự tồn tại trong DataFrame tránh lỗi Key Error
        existing_cols = [col for col in columns_to_keep if col in df.columns]
        df = df[existing_cols].copy()
        
        # Rename columns cho thông dụng và quy chuẩn chung cho bảng DB / CSV
        rename_mapping = {
            "reviewsCount": "reviewCount",
            "categoryName": "category"
        }
        df.rename(columns=rename_mapping, inplace=True)
        
        # Mapping tọa độ lat/lng từ Dict Object lồng nhau 'location' ra hai cột độc lập
        if 'location' in df.columns:
            df['lat'] = df['location'].apply(lambda x: x.get('lat') if isinstance(x, dict) else None)
            df['lng'] = df['location'].apply(lambda x: x.get('lng') if isinstance(x, dict) else None)
            df.drop(columns=['location'], inplace=True) # Xóa cột location thô đi cho nhẹ db
            
        # Cơ chế Deduplicate: Ngăn ngừa một công ty hiện 2 lần trên map cùng khu vực hoặc số điện thoại
        before_dedup = len(df)
        
        # Chỉ dùng những cột tồn tại để lọc trùng (tránh lỗi KeyError nếu API không có field 'phone' như Google TextSearch)
        dup_subset = ['title']
        if 'phone' in df.columns:
            dup_subset.append('phone')
        
        df.drop_duplicates(subset=dup_subset, keep='first', inplace=True)
        after_dedup = len(df)
        
        logger.info(f" Làm sạch dữ liệu rác/trùng lặp thành công. Đã loại bỏ ({before_dedup - after_dedup}) bản ghi duplicate.")
        logger.info(f" Đội Sales còn lại {after_dedup} bản ghi thực tế độc lập duy nhất.")
        
        # Fill None values
        df.fillna('', inplace=True)
        
        return df
