# 🇻🇳 VietnamLeadExtractor (VLE)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**VietnamLeadExtractor** là siêu công cụ CLI mã nguồn mở (MIT) giúp bạn tự động trích xuất hàng ngàn leads B2B từ Google Maps và dùng trí tuệ nhân tạo (Hugging Face Zero-shot AI) để tự động phân loại, chấm điểm lead (High/Medium/Low Quality) dành riêng cho developer, freelancer, agency và startup Việt Nam.

> *Món quà này dành cho cộng đồng Builder Việt - những người chuyên xây dựng hệ thống tự động để tăng trưởng.*

---

## 🍵 Chưng Cất Kiến Thức (Governance + AI Tăng Tốc)

> **"Không có governance thì chạy nhanh đến mấy cũng lao xuống vực"** - *Phong cách TinySDLC*

Dự án này được thiết kế theo tư duy **TinySDLC**:
- **Tiny Governance**: Code tuân thủ PEP8 100%, có type hints (`typing`), sử dụng Docstring Google Style rõ ràng. Chúng tôi không in log một cách vô tội vạ bằng `print`, tất cả dùng custom `logger`.
- **Tiny Architecture**: Tách bạch logic ra 3 class chính: `Scraper` (Giao tiếp API), `Processor` (Xử lý dữ liệu Pandas), `Classifier` (Hugging Face AI). Rất dễ để bạn vào đóng góp tiếp.
- **AI Tăng Tốc**: Bạn cào ngàn leads nhưng chỉ 100 leads tiềm năng? Hệ thống sử dụng *Zero-shot Classification* để tự chấm điểm dựa vào ngôn ngữ, rating và hạng mục của doanh nghiệp, giúp bạn chắt lọc leads xịn nhất ngay từ đầu.
- **Localisation**: Tiếng Việt được ưu tiên! Lưu `.csv` chuẩn utf-8-sig để khách hàng mở Excel không bị lỗi phông chữ.

## 🎯 Use Cases Tại Việt Nam

- **B2B Tech Startup**: "Tìm tất cả các 'bệnh viện' tại 'Hà Nội' để sale phần mềm quản lý y tế".
- **F&B Agency**: "Lọc các 'nhà hàng' có đánh giá dưới 3 sao tại 'TP.HCM' để chào gói setup lại thương hiệu".
- **Sản Xuất / Phân Phối**: "Săn các 'xưởng mộc' tại 'Bình Dương' để gửi mẫu gỗ/báo giá".

## 🚀 Hướng Dẫn Sử Dụng (Dành cho người mới)

Dự án này được thiết kế theo đúng triết lý "Nhỏ nhưng dùng được", chạy hoàn toàn trên máy cá nhân cục bộ (Local) của bạn. Hệ thống hoạt động như một Trợ lý AI tự động để quét, phân tích và lọc leads B2B từ bản đồ.

### 1. Chuẩn Bị Môi Trường
Đảm bảo máy tính của bạn đã cài đặt Python 3.10 trở lên.

Mở Terminal (Command Prompt hoặc PowerShell) và chạy các dòng lệnh sau để tải dự án về máy:
```bash
git clone https://github.com/your-username/VietnamLeadExtractor.git
cd VietnamLeadExtractor
```

Tạo một môi trường ảo (Virtual Environment) để cài đặt các thư viện không bị xung đột với hệ thống:
```bash
python -m venv venv
```

Kích hoạt môi trường vừa tạo:
- **Windows**: `.\venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

Tiếp theo, hãy cài đặt toàn bộ "vũ khí" cần thiết bằng lệnh:
```bash
pip install -r requirements.txt
```

### 2. Cấu Hình Sức Mạnh (API Keys)
Chìa khóa để bật bộ não AI và hệ thống quét là file `.env`. Nhân bản (copy) nội dung tệp `.env.example` ở dự án ra thành tự tạo mới tên `.env` ngay trong thư mục gốc (ngang hàng README.md) và dán thông tin của bạn vào:

```env
# 1. API Key của Google (Google Maps / Places API)
API_KEY=AIzaSy_CUA_BAN_O_DAY

# 2. Endpoint của Google Places Text Search (Hoặc API tương tự bạn muốn dùng)
API_ENDPOINT=https://maps.googleapis.com/maps/api/place/textsearch/json
```

### 3. Vận Hành Tác Chiến
Chúng tôi đã setup sẵn hệ thống CLI mạnh mẽ để bạn có thể sử dụng sức mạnh Agent tùy theo nhu cầu:

#### a. Quét Mẫu Dữ Liệu Live (Khai phá Leads Mới)
File này sẽ kéo dữ liệu của các doanh nghiệp kinh doanh tại thời điểm thực theo khu vực bạn chọn và xuất ra thành tệp Excel (CSV) sau khi AI đã phân tích "Nhãn chất lượng".
```bash
python main.py --keyword "nhà cung cấp phần mềm" --province "TP.HCM" --max 100 --output csv
```

#### b. Quét Export JSON để Đẩy Vào Database (CRM Integration)
Chế độ này xuất dữ liệu JSON chuẩn hóa, bạn có thể dễ dàng map cấu trúc để import thẳng vào Zoho CRM, Hubspot hoặc Database đội Dev, tiết kiệm tối đa rủi ro nhập tay.
```bash
python main.py --keyword "nhà hàng cao cấp" --province "Hà Nội" --max 200 --output json
```

## 🔌 Tích Hợp Zoho CRM (Có Sẵn Mẫu)
Trong `main.py` đã có sẵn placeholder comment dành cho việc đút thẳng danh sách cào được vào Zoho CRM. Bạn chỉ việc thêm token OAuth vào và mở comment.

## 💡 Lời Kêu Gọi Cộng Đồng
Đây là dự án mở 100% dành cho người Việt. Chúng ta rất cần sự ủng hộ của các bạn:
- Hãy bấm **⭐ Star** repo này!
- Có ý tưởng hay? Hãy mở **Issue**!
- Thích code? Gửi **Pull Request (PR)**!

*Vì một cộng đồng Builder Việt vững mạnh.*
