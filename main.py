import os
import click
from src.core.scraper import GoogleMapsScraper
from src.core.processor import DataProcessor
from src.core.ai_classifier import LeadClassifier
from src.utils.logger import get_logger

logger = get_logger(__name__)

@click.command()
@click.option('--keyword', required=True, help="Từ khóa tìm kiếm (VD: 'nhà hàng').")
@click.option('--province', default="", help="Tỉnh/Thành phố/Vị trí (VD: 'Hà Nội').")
@click.option('--max', 'max_results', default=100, type=int, help="Số kết quả tối đa (Default: 100).", show_default=True)
@click.option('--output', type=click.Choice(['csv', 'json']), default='csv', help="Định dạng xuất file.", show_default=True)
def cli(keyword: str, province: str, max_results: int, output: str):
    """
    VietnamLeadExtractor
    Công cụ xuất dữ liệu doanh nghiệp B2B từ Google Maps tại Việt Nam
    và sử dụng AI (Hugging Face) để phân loại/đánh giá (chất lượng Cao/Trung Bình/Thấp).
    """
    logger.info("=== Bắt đầu khởi chạy VietnamLeadExtractor ===")
    
    # 1. Scrape dữ liệu
    scraper = GoogleMapsScraper()
    raw_data = scraper.search(keyword=keyword, province=province, max_results=max_results)
    
    # 2. Làm sạch & định dạng dữ liệu (bằng Pandas)
    processor = DataProcessor()
    df = processor.process(raw_data)
    
    if df.empty:
        logger.warning("Không có dữ liệu trích xuất. Dừng chương trình.")
        return
        
    # 3. Chấm điểm & phân loại AI (Zero-shot classification)
    classifier = LeadClassifier()
    df_classified = classifier.classify_leads(df)
    
    # 4. Xuất file kết quả
    filename_part = f"{province or 'all'}_{keyword.replace(' ', '_')}".lower()
    filename = f"leads_{filename_part}.{output}"
    
    if output == 'csv':
        df_classified.to_csv(filename, index=False, encoding='utf-8-sig') # Định dạng utf-8-sig tương thích tốt với Excel
    else:
        df_classified.to_json(filename, orient='records', force_ascii=False, indent=4)
        
    logger.info(f" Hoàn thành! File đã được lưu tại: {filename}")
    logger.info("Tiếp theo: Bạn có thể import dữ liệu này vào hệ thống CRM (VD: Zoho, Hubspot, Bitrix24).")
    
    # [Tích hợp sẵn Zoho CRM Placeholder]
    # import requests
    # url = "https://www.zohoapis.com/crm/v2/Leads"
    # headers = {"Authorization": "Zoho-oauthtoken YOUR_ZOHO_TOKEN_HERE"}
    # payload = {
    #     "data": [
    #         {"Company": row['title'], "Last_Name": row['title'], "Phone": row['phone']} 
    #         for _, row in df_classified.iterrows()
    #     ]
    # }
    # response = requests.post(url, json=payload, headers=headers)
    # logger.info(f"Zoho push status: {response.status_code}")

if __name__ == '__main__':
    cli()
