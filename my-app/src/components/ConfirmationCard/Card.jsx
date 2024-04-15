import React from 'react';
import './Card.css';

const Card = ({ message, handleConfirm, handleCancel }) => {
  return (
    <div className='confirmation-card'>
      <p>{message}</p>
      <div className='button-container'>
        <button onClick={handleConfirm}>Confirm</button>
        <button onClick={handleCancel}>Cancel</button>
      </div>
    </div>
  );
};

export default Card;