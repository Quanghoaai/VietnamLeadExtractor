# Tiêu chuẩn Dự án (Governance Rules)

Dự án này tuân thủ các quy tắc nghiêm ngặt để đảm bảo chất lượng, khả năng bảo trì và tính mở.

1.  **License**: Mọi đóng góp đều phải tuân theo MIT License. Mọi thay đổi không được hạn chế quyền sử dụng thương mại của cộng đồng.
2.  **PEP8**: Code Python phải tuân thủ chuẩn PEP8. Ưu tiên sử dụng `flake8` hoặc `black` để định dạng code thống nhất.
3.  **Type Hints**: Bắt buộc sử dụng type hints cho toàn bộ các tham số và giá trị trả về của mọi function/method (`from typing import List, Dict, ...`).
4.  **Logging**: Không sử dụng lệnh `print()`. Bắt buộc sử dụng instances `logger` khởi tạo từ `src.utils.logger`.
5.  **Docstring**: Tuân thủ chuẩn Google Style cho docstring để auto-generator như Sphinx hoặc MkDocs có thể đọc dễ dàng.
6.  **Ngôn ngữ Comment**: Bắt buộc viết string tĩnh và block bình luận giải thích thuật toán bằng *tiếng Việt* rõ ràng, mạch lạc, dễ hiểu đối với các developers Việt Nam. Các hàm (functions/variables) bằng tiếng Anh chuyên dụng.

*Antigravity agent sẽ giám sát và tự động enforce các quy tắc này tại nhánh Main/Master.*
