'use strict';

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