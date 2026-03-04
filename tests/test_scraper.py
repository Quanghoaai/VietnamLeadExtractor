import pytest
import pandas as pd
from unittest.mock import MagicMock
from src.core.processor import DataProcessor

def test_processor_deduplication():
    # Giả lập data nhận từ Apify
    processor = DataProcessor()
    raw_data = [
        {"title": "Công ty TNHH A", "phone": "0981234567", "location": {"lat": 21.0, "lng": 105.8}},
        {"title": "Công ty TNHH A", "phone": "0981234567", "location": {"lat": 21.0, "lng": 105.8}}, # Bản ghi trùng lặp
        {"title": "Công ty Tư Vấn B", "phone": "0912345678", "location": {"lat": 10.7, "lng": 106.6}},
    ]
    
    # Xử lý
    df = processor.process(raw_data)
    
    # Kì vọng: Trùng sẽ bị loại, còn lại 2 dòng
    assert len(df) == 2, "Deduplication thất bại: Vẫn còn bản ghi trùng."
    assert "lat" in df.columns, "Tách tọa độ lat thất bại."
    assert "lng" in df.columns, "Tách tọa độ lng thất bại."

def test_empty_raw_data():
    processor = DataProcessor()
    df = processor.process([])
    assert df.empty, "DataFrame phải rỗng khi input rỗng."
