# Hệ thống Nhận diện Văn bản từ Ảnh (OCR)

## Yêu cầu hệ thống
- Python 3.8+ (cho backend)
- Node.js 14+ (cho frontend)
- Tesseract OCR đã cài đặt (hướng dẫn: https://github.com/tesseract-ocr/tesseract)

## Cài đặt dependencies
1. Backend:
   - Chuyển đến thư mục backend: `cd backend`
   - Cài đặt: `pip install -r requirements.txt`

2. Frontend:
   - Chuyển đến thư mục frontend: `cd ../frontend`
   - Cài đặt: `npm install`

## Chạy dự án
1. Chạy backend (Flask):
   - Từ thư mục backend: `python app.py`
   - Server sẽ chạy trên http://127.0.0.1:5000/

2. Chạy frontend (React):
   - Từ thư mục frontend: `npm start`
   - Ứng dụng sẽ chạy trên http://localhost:3000/

3. Kiểm tra:
   - Truy cập http://localhost:3000/ để upload file.
   - File sẽ được gửi đến backend, và kết quả sẽ hiển thị trên trang.

## Lưu ý
- Độ chính xác OCR: Thêm logic tinh chỉnh Tesseract trong app.py để đạt ≥80%.
- Hỗ trợ ngôn ngữ: Sử dụng tham số lang trong pytesseract.
- Code này chỉ là khung, bạn cần thêm logic chi tiết cho OCR.