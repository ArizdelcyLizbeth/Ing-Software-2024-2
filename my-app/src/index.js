import React from 'react';
import { createRoot } from 'react-dom';
import './index.css';
import App from './App/App';
import reportWebVitals from './reportWebVitals';

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Si deseas comenzar a medir el rendimiento de tu aplicación, pasa una función
// para registrar resultados (por ejemplo: reportWebVitals(console.log))
// o enviar a un punto final de análisis. Aprende más en: https://bit.ly/CRA-vitals
reportWebVitals();
