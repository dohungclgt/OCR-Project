# Hệ thống Nhận diện Văn bản từ Ảnh (OCR)

## Yêu cầu hệ thống
- Python 3.8+ (cho backend)
- Node.js 14+ (cho frontend)
- Tesseract OCR đã cài đặt (hướng dẫn: https://github.com/tesseract-ocr/tesseract)

## Cài đặt dependencies
1. Backend:
   - Chuyển đến thư mục backend: `cd backend`
   - Cài đặt: `pip install -r requirements.txt`
   - chạy app.py để listen localhost (không chạy trực tiếp ở đó)

2. Frontend:
   - Chuyển đến thư mục frontend: `cd ../frontend`
   - Cài đặt: `npm install`
   - Yêu cầu cài NodeJS để có thể hoạt động tốt

## Chạy dự án
1. Chạy backend (Flask):
   - Từ thư mục backend: `python app.py`
   - Server sẽ chạy trên http://127.0.0.1:5000/

2. Chạy frontend (React):
   - Từ thư mục frontend: `npm start`
   - Ứng dụng sẽ chạy trên http://localhost:3000/
=> Lưu ý: Nếu chạy terminal trên Visual Studio Code thì hãy tạo 2 Terminal để nó hoạt động (1 Terminal của app.py và 1 Terminal để chạy npm)
3. Kiểm tra:
   - Truy cập http://localhost:3000/ để upload file.
   - File sẽ được gửi đến backend, và kết quả sẽ hiển thị trên trang.
   - Hiện tại chưa có API của Google Vision nên upload file hiện đang lỗi, sẽ tìm cách xử lý sau

## Lưu ý
- Độ chính xác OCR: Thêm logic tinh chỉnh Tesseract trong app.py để đạt ≥80%.
- Hỗ trợ ngôn ngữ: Sử dụng tham số lang trong pytesseract.
- Không cần để ý thư mục node_modules vì nó là thư viện của js
