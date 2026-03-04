# Hướng Dẫn Sử Dụng VietnamLeadExtractor

Tài liệu này hướng dẫn chi tiết cách để bạn khai thác mạnh mẽ tool này cho phễu sales B2B.

## 1. Lấy dữ liệu theo Tỉnh Thành (Local Search)

**Từ khóa khuyên dùng:** 
- `nhà cung cấp <ngành nghề>`
- `xưởng sản xuất <ngành hàng>`
- `cửa hàng <đồ dùng>`
- `bệnh viện`, `phòng khám`, `trung tâm đăng kiểm`

**Cú pháp:**
```bash
python main.py --keyword "công nghệ phần mềm" --province "Tân Bình, TP.HCM" --max 300
```
- Công cụ sẽ tự nối keyword và province để tìm: *"công nghệ phần mềm tại Tân Bình, TP.HCM"*

## 2. Xuất JSON để Import vào Database (MongoDB, PostgreSQL)

Mặc định xuất ra CSV (Encoding: UTF-8-SIG để Excel đọc tiếng Việt). Nếu bạn là Dev, muốn import JSON vào Database:
```bash
python main.py --keyword "nhà hàng cao cấp" --output json
```

## 3. Xem xét Điểm AI (Lead Quality)
Trong file CSV sinh ra, hãy chú ý cột cuối cùng `lead_quality`.
Lọc các dòng có `lead_quality == High` để đội Telesales liên hệ trước. Các dòng có chữ `Low` thường là doanh nghiệp bị đánh giá rất thấp (dưới 3 sao, nhiều review chửi rủa), hoặc doanh nghiệp đã phá sản/chuyển địa điểm.
