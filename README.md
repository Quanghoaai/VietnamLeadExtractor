<div align="center">
  <img src="https://img.icons8.com/color/120/000000/google-maps-new.png"/>
  <h1>🚀 VietnamLeadExtractor (B2B Leads x AI)</h1>
  <p><strong>Bóc tách & Thẩm định Dữ liệu Khách hàng B2B Doanh nghiệp tại Việt Nam bằng Trí tuệ Nhân tạo</strong></p>
  
  <p>
    <a href="https://github.com/Quanghoaai/VietnamLeadExtractor/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
    </a>
    <a href="https://python.org">
      <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+" />
    </a>
    <img src="https://img.shields.io/badge/AI-Hugging_Face-orange.svg" alt="Hugging Face LLM" />
    <img src="https://img.shields.io/badge/LLM-Gemini_2.5_Flash-purple.svg" alt="Gemini 2.5 Flash" />
  </p>
</div>

---

## 🎯 Giới thiệu Dự án

**VietnamLeadExtractor** không chỉ là một công cụ cào dữ liệu thông thường. Đây là một **Agent tự động** (Autonomous Agent) thiết kế chuyên biệt cho giới Developer, Freelancer, Agency, và Startup Việt Nam. Công cụ giúp bạn khai thác chính xác 100% Leads của các doanh nghiệp thực có mặt trên bản đồ, đồng thời gắn kèm _"Bộ Não AI"_ để phân tích tiềm năng của họ.

> 💡 **"Nhỏ nhưng dùng được"** – Bạn không cần máy tính siêu khủng, không cần đăng nhập lằng nhằng. Mọi thứ vận hành ngầm 100% (Headless) và cực kỳ bảo mật tại máy Local của bạn!

### 🔥 Tính năng "Ngầu" Nhất (Killer Features)
- **⚡ Local API Fast-Track**: Cào trực tiếp thông qua API với tốc độ xé gió. Tự động deduplicate (khử trùng lặp) thông minh.
- **🤖 Tích hợp Trí tuệ Nhân tạo Kép**:
  - **Local AI (MiniLM)**: Sử dụng Hugging Face NLP (Zero-shot classification) siêu nhẹ, chạy hoàn toàn offline bằng CPU của bạn để _chấm điểm khách hàng_ (Chất lượng Cao / Trung bình / Thấp) dựa trên sức ảnh hưởng của doanh nghiệp đó.
  - **Auto Fallback to Gemini 2.5 Flash**: Nếu Google Maps API Key của bạn bị chặn, hệ thống tự động bẻ lái sang dùng Generative AI của Gemini ngầm ở phía dưới để tổng hợp danh sách Data trả về cho bạn. Cực kỳ bá đạo!
- **🌐 Xuất File Đa Định Dạng**: Hỗ trợ nén data chuẩn xác ra **CSV**, **JSON**, và nay tích hợp cả **Excel (.XLSX)** để ném thẳng vào Zoho, Bitrix24 hay Hubspot.

---

## 🛠 Hướng Dẫn Sử Dụng (Dành cho người mới)

### 1. Chuẩn Bị Môi Trường
Đảm bảo máy tính của bạn đã cài đặt Python 3.10 trở lên.

Mở Terminal (Command Prompt hoặc PowerShell) và chạy các dòng lệnh sau để tải dự án về máy:

```bash
git clone https://github.com/Quanghoaai/VietnamLeadExtractor.git
cd VietnamLeadExtractor
```

Tạo một môi trường ảo (Virtual Environment) để cài đặt các thư viện siêu sạch:

```bash
python -m venv venv
```

Kích hoạt môi trường:
- **Windows**: `.\venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

Cài đặt vũ khí (Dependencies):
```bash
pip install -r requirements.txt
```

### 2. Cấu Hình Khởi Động (Trái Tim Của Hệ Thống)
Bạn cần API Key để chương trình biết nó đang phục vụ ai.
1. Copy file `.env.example` thành `.env`.
2. Mở file `.env` lên và điền KEY của bạn vào. 
> *Bí kíp: Dự án chấp nhận cả khóa truyền thống của Google Maps API hoặc khóa API Gemini AI dán vào.*

## 🚀 Thao Tác Chạy Lệnh

Sử dụng cú pháp thần thánh sau để khai phá Data ở bất kỳ vị trí địa lý nào:

**Xuất ra file CSV (Mặc định):**
```bash
python main.py --keyword "công nghệ phần mềm" --province "Hà Nội" --max 50
```

**Xuất ra Excel (XLSX) cho dân Sales/Marketing:**
```bash
python main.py --keyword "spa thẩm mỹ" --province "Đà Nẵng" --max 100 --output excel
```

**Xuất ra định dạng JSON cho dân Coder nhúng API:**
```bash
python main.py --keyword "bất động sản" --province "TP.HCM" --max 20 --output json
```

---

## 🧠 Chưng Cất Kiến Thức (Góc độ Kiến trúc - TinySDLC)

Hệ thống được thiết kế theo nguyên lý **Modular** (Module hóa tách biệt hoàn toàn):
- `scraper.py`: Nhọc nhằn việc gọi Data thô, tích hợp Auto-Fallback LLM (Gemini 2.5 Flash).
- `processor.py`: Trạm xử lý Pandas (DataFrame) siêu sạch, gọt dũa những dữ liệu bẩn và loại trùng lặp.
- `ai_classifier.py`: Trái tim AI Zero-shot Model (Multilingual-MiniLMv2-L6) tải thẳng vào RAM máy bạn, hiểu liền Tiếng Anh/Tiếng Việt mà không cần Train rườm rà. Nó thay bạn trả lời câu hỏi *"Lead này có giàu không?"*

---

## 🤝 Giấy Phép (License)
Toàn bộ mã nguồn mở 100% tuân thủ **MIT License**. Bạn có quyền tải về, xào nấu, kiếm tiền, và đập đi xây lại tùy thích!
Hãy cho dự án **1 🌟 Star** nếu nó giúp ích được cho công việc của bạn nhé!

---
*Phát triển bởi Quanghoaai - Cộng đồng Python Việt Nam.*
