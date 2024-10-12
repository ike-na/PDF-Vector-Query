import React, { useState, ChangeEvent, useEffect } from 'react';
import './PdfUploader.css';
import QuestionForm from './QuestionForm';
import Ball from './Ball';

const PdfUploader: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [fileName, setFileName] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isDone, setIsDone] = useState<boolean>(false);
  const [progress, setProgress] = useState<number>(0);
  const [message, setMessage] = useState<string>('');  
  const [isQuestioning, setIsQuestioning] = useState<boolean>(false);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setFile(event.target.files[0]);
      setFileName(event.target.files[0].name);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Please select a PDF file to upload.');
      return;
    }
    setIsLoading(true);
    setIsDone(false);
    setProgress(0);

    const formData = new FormData();
    formData.append('pdf', file);
    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Upload failed');
      }
      setMessage('');
    } catch (error) {
      setMessage(`Error uploading file: ${error}`);
    }

    // Simulating upload process with progress
    for (let i = 0; i <= 100; i += 2) {
      await new Promise(resolve => setTimeout(resolve, 60));
      setProgress(i);
    }
    setIsLoading(false);
    setIsDone(true);
    setTimeout(() => {setIsQuestioning(true);}, 3500);
  };

  useEffect(() => {
    if (isDone) {
      const timer = setTimeout(() => setIsDone(false), 3500);
      return () => clearTimeout(timer);
    }
  }, [isDone]);

  // Cleanup function to destroy chroma_vector_db on component unmount
  useEffect(() => {
    return () => {
        destroyChromaVectorDB(); 
    };
}, []);

const destroyChromaVectorDB = async () => {
    try {
        const response = await fetch('http://localhost:5000/api/chroma-vector-db', {
            method: 'DELETE',
        });
        if (404 === response.status) {
            console.log('Chroma vector DB not found');
        }
        const data = await response.json();
        console.log(data.message);
    } catch (error) {
        console.error(`Error: ${error}`);
    }
};


  const renderProgressBar = (progress: number) => {
    const barWidth = 50;
    const filledWidth = Math.floor((progress / 100) * barWidth);
    const emptyWidth = barWidth - filledWidth;
    return `${progress}% [${'■'.repeat(filledWidth)}${''.repeat(emptyWidth)}]`;
  };

  if (isQuestioning) {
    return <QuestionForm onClose={() => setIsQuestioning(false)} />; 
  }

  return (
    <div className='big-container'>
      <Ball />
  
    <div className="pdf-uploader">
      <p>{'> SELECT PDF FILE:'}</p>
      <label className="file-input-label">
    Choose file
    <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
        className="file-input"/>
    </label>
    {fileName && <p className="selected-file"> {'>'} Selected file: {fileName}</p>}
      <button
        onClick={handleUpload}
        disabled={!file}
        className="upload-button"
      >
        {isLoading ? 'UPLOADING...' : 'UPLOAD PDF'}
      </button>
      {isLoading && (
        <div className="progress-container">
          <p>{'UPLOADING...'}</p>
          <div className="progress-bar">
            {renderProgressBar(progress)}
          </div>
        </div>
      )}
      {isDone && (
        <div className="completion-message">
          {'> UPLOAD COMPLETE'}
        </div>
      )}
      {message && <p>{message}</p>} 
    </div>
    </div>
  );
};

export default PdfUploader;
