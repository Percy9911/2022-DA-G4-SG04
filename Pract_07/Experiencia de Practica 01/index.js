
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function MyApp() {
  const [likes, setLikes] = useState(0);
  const [dislikes, setDisLikes] = useState(0);

  return (
    <div id="box">
      <Condicion />
      <div>
        <button onClick={() => setLikes(likes + 1)}>likes {likes}</button>
        <button onClick={() => setDisLikes(dislikes + 1)}>dislikes {dislikes}</button>
      </div>
    </div>
  );
}

function Condicion() {
  const [cond, setCond] = useState(false);

  return (
    <div>
      <div id="b"></div>
      <div>
        <button onClick={() => setCond(!cond)}>descripcion</button>
        {
          cond &&
          <h5>descripcion del mensaje</h5>
        }
      </div>
    </div>
  )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyApp />);

