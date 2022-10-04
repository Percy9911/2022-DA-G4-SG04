import React, { useLayoutEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { directive } from '@babel/types';
import { useState } from 'react';

class CambiarColor extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      desc: 'negro',
    };
  }  

  cambiarRojo = () =>{
    this.setState({
      desc: this.state.desc = 'rojo'
    })
    document.getElementById('tit').style = 'color: red';
  }

  cambiarVerde = () =>{
    this.setState({
      desc: this.state.desc = 'verde'
    })
    document.getElementById('tit').style = 'color: green';
  }

  cambiarAzul = () =>{
    this.setState({
      desc: this.state.desc = 'azul'
    })
    document.getElementById('tit').style = 'color: blue';
  }

  cambiarRosa = () =>{
    this.setState({
      desc: this.state.desc = 'rosa'
    })
    document.getElementById('tit').style = 'color: hotpink';
  }

  cambiarNaranja = () =>{
    this.setState({
      desc: this.state.desc = 'naranja'
    })
    document.getElementById('tit').style = 'color: orange';
  }

  render(){
    const {desc} = this.state;
    return (
      <div id = 'cont'>
        <h1 id = 'tit'> Hola soy de color {desc} </h1>
        <div id = 'botones'>
          <button id = 'rojo' onClick={this.cambiarRojo}>ROJO</button>
          <button id = 'verde' onClick={this.cambiarVerde}>VERDE</button>
          <button id = 'azul' onClick={this.cambiarAzul}>AZUL</button>
          <button id = 'rosa' onClick={this.cambiarRosa}>ROSA</button>
          <button id = 'naranja' onClick={this.cambiarNaranja}>NARANJA</button>
        </div>
      </div>
    )
  }
}

function Oracion(prop) {
  const {nombre, pais} = prop;
  const [tam, setTam] = useState(10);

  return(
    <div id = 'cont'>
      <h1 id ='tit2' onClick={() => setTam(tam + 1)}>Hola soy {nombre} y soy de {pais} y mi edad es {tam} </h1>
    </div>
  )
}


function Exp04() {
  return (
    <div>
      <div>
        <h2>ESTADO CON CLASES</h2>
        <CambiarColor/>
      </div>
      <div>
        <h2>ESTADO CON USESTATE</h2>
        <Oracion nombre = "Luz" pais = "Bolivia"/>
      </div>
    </div>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Exp04/>);

