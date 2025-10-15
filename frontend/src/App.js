// frontend/src/App.js
import React, { useState } from 'react';
import './style.css'; 

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert('Please select a file');
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await fetch('/upload', {  // Gửi đến backend Flask
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data.result);  // Hiển thị kết quả
    } catch (error) {
      console.error('Error uploading file:', error);
      setResult('Error occurred');
    }
  };

  return (
    <div className="App">
      <h1>OCR Application</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Process</button>
      <h2>Result:</h2>
      <p>{result}</p>  // Hiển thị kết quả OCR
    </div>
  );
}

export default App;

