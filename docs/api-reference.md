# API Reference Documents

Tài liệu này dành cho các Dev Việt Nam muốn nhảy vào xem code và contribute.

## Cấu trúc Module

- `src.core.scraper.GoogleMapsScraper`
  - Giao tiếp với API của Apify qua package chính thức `apify-client`.
  - Class có khả năng Retry và Exception Handling cơ bản khi network chết.
- `src.core.processor.DataProcessor`
  - Phụ trách bóp nhỏ Data, loại bỏ các dictionary nested của Google, chuyển hóa thành Table (Pandas DataFrame) siêu bẹt (Flat).
- `src.core.ai_classifier.LeadClassifier`
  - Zero-shot classification. Sử dụng Pipeline của Hugging Face. Không cần train, tự phân tích Text Semantic.
- `src.utils.logger`
  - Đóng gói Logging. Cấm dùng `print` rác terminal, hãy `from src.utils.logger import get_logger`.
