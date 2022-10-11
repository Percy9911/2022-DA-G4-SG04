import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function Mover() {
  const [color, setColor] = useState("blue")
  const [cont1, setCont1] = useState(0)
  useEffect(() => {
    function onMouse(e) {
      if (e.clientX < window.innerWidth) {
        setColor('red')
      }
    }

    document.getElementById('box').addEventListener("mousemove", onMouse);

  }, []);

  return (
    <div id='container'>
      <div id='box' style={{ backgroundColor: color }} onClick={() => setCont1(cont1 + 1)} onMouseLeave={() => setColor("blue")}> {cont1}</div>
      <h3>Presiona el cuadrado</h3>
    </div >
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Mover />);


