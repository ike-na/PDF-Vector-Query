import React, { useState } from 'react';
import './QuestionForm.css';
import Ball from './Ball';

interface QuestionFormProps {
  onClose: () => void;
}

const QuestionForm: React.FC<QuestionFormProps> = ({ onClose }) => {
  const [question, setQuestion] = useState<string>('');
  const [answer, setAnswer] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleQuestionSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      });
      if (!response.ok) {
        throw new Error('Error asking question');
      }
      const data = await response.json();
      setAnswer(data.answer);
      setError('');
    } catch (err) {
      setError(`Failed to get an answer: ${err}`);
    }
  };

  return (
    <div className='big-container'>
      <Ball />
      <div className="question-form">
        <h3>{'> ASK YOUR QUESTION.'}</h3>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="What do you want to know?"
        />
        <button onClick={handleQuestionSubmit}>
          {'Submit Question'}
        </button>
        {answer && <p className="answer">{`Answer: ${answer}`}</p>}
        {error && <p className="error">{error}</p>}
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default QuestionForm;
