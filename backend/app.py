from flask import Flask, request, jsonify, render_template
import os
app = Flask(__name__)
# Cấu hình thư mục upload (có thể thay đổi)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# Route chính: Hiển thị form upload (hoặc gọi từ frontend)
@app.route('/')
def index():
    return render_template('index.html')  # Render trang HTML cơ bản
# Route để xử lý upload file và OCR
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Lưu file tạm thời (khung code, chưa xử lý OCR)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    #TODO Khung code cho xử lý OCR (chưa implement logic chi tiết)
    
    result = "Khung code: Kết quả OCR sẽ ở đây" 
    
