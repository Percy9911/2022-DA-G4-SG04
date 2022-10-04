import { directive } from '@babel/types';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

const Seccion = (props) => {
  return(
    <div>
      <h2> --------------------- {props.titu} --------------------- </h2>
    </div>
  );
}

class Caja extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      desc:""
    }
  }

  
camClaro = () => {
  this.setState({
    desc:"CLARO"
  });
  document.getElementById('caja').style = 'background-color: pink';
  document.getElementById('cam').style = 'color: darkred'
}
camOscuro = () => {
  this.setState({
    desc:"OSCURO"
  });
  document.getElementById('caja').style = 'background-color: darkred';
  document.getElementById('cam').style = 'color: pink'
}

  render(){
    return (
      <div id ='caja'>
        <h1 id='cam'>TEMA {this.state.desc}</h1>
        <div>
          <button id='claro' onClick={this.camClaro}>CLARO</button>
          <button id='oscu' onClick={this.camOscuro}>OSCURO</button>
        </div>
      </div>
    );
  }
}

const temp = ['verano', 'invierno', 'otoño', 'primavera'];

function MostTem(props){
  const temp = props.temp;
  const item = temp.map((a) => <li>{a}</li>);
  return (
    <div id = 'caja'>
      <h3>Temporada</h3>
      <ul>{item}</ul>
    </div>
  )
}


function Ejer01() {
  return(
    <div>
      <Seccion titu='Visor 01'/>
      <Caja/>
      <Seccion titu = 'Visor 02'/>
      <MostTem temp = {temp}/>
    </div>
  )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Ejer01/>);

