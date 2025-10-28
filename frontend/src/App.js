import React, { useState } from 'react';
import { uploadImage } from './api';

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Vui lòng chọn file!");
      return;
    }
    setLoading(true);
    try {
      const result = await uploadImage(file);
      setText(result.text);
    } catch (err) {
      alert("Lỗi OCR: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ margin: '50px', textAlign: 'center' }}>
      <h2>🧠 OCR Text Extractor</h2>
      <input
        type="file"
        accept="image/*,application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? 'Đang xử lý...' : 'Nhận diện chữ'}
      </button>

      <div style={{
        marginTop: '30px',
        padding: '10px',
        border: '1px solid #ccc',
        whiteSpace: 'pre-wrap',
        textAlign: 'left',
        maxWidth: '800px',
        marginInline: 'auto'
      }}>
        {text || 'Kết quả OCR sẽ hiển thị ở đây...'}
      </div>
    </div>
  );
}

export default App;
