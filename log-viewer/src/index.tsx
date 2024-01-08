import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App'; // Certifique-se de que App.tsx está no mesmo diretório
import reportWebVitals from './reportWebVitals';

const rootElement = document.getElementById('root');

if (!rootElement) throw new Error('Falha ao encontrar o elemento root');

const root = ReactDOM.createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
