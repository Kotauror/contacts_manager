import React from "react";

class App extends React.Component {
  constructor() {
    super();

    this.state = {
      contacts: []
    }
  }
  render () {
    return <p> Welcome to the contacts manager!</p>
  }
}

export default App;
