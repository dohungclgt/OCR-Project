from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from ocr import ocr_from_path
from pathlib import Path
import logging

# setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# config
BASE_DIR = Path(__file__).parent
UPLOAD_FOLDER = BASE_DIR / 'uploads'
UPLOAD_FOLDER.mkdir(exist_ok=True)
ALLOWED_EXT = {'.png', '.jpg', '.jpeg', '.pdf'}

app = Flask(__name__)
CORS(app)  # allow all origins for dev; tighten in production
app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXT

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/upload', methods=['POST'])
def upload():
    """
    Expects multipart/form-data:
      - file: file
      - lang: optional (default 'eng+vie')
    Returns JSON: { filename, text }
    """
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'}), 400
    f = request.files['file']
    if f.filename == '':
        return jsonify({'error': 'no selected file'}), 400
    if not allowed_file(f.filename):
        return jsonify({'error': 'file type not allowed'}), 400

    filename = secure_filename(f.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(save_path)
    logger.info("Saved upload to %s", save_path)

    lang = request.form.get('lang', 'eng+vie')

    try:
        text = ocr_from_path(save_path, lang=lang)
    except Exception as e:
        logger.exception("OCR failed")
        return jsonify({'error': str(e)}), 500

    # optional: save text file beside upload
    txt_path = save_path + '.txt'
    with open(txt_path, 'w', encoding='utf-8') as fh:
        fh.write(text)

    return jsonify({'filename': filename, 'text': text})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    filename = secure_filename(filename)
    txt_path = os.path.join(app.config['UPLOAD_FOLDER'], filename + '.txt')
    if not os.path.exists(txt_path):
        return jsonify({'error': 'not found'}), 404
    return send_file(txt_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
