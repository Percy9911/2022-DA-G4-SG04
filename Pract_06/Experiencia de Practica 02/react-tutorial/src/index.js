
import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import './index.css'
class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Hola, Soy Daniel!</h1>
      </div>
    )
 }
}
ReactDOM.render(<App />, document.getElementById('root'))

const e = React.createElement;

class reactExp01 extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'Presionaste este boton, gracias.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Presiona el boton'
    );
  }
}
const domContainer = document.querySelector('#reactExp01');
const root = ReactDOM.createRoot(domContainer);
root.render(e(reactExp01));