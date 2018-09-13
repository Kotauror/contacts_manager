import React, { Component } from "react";
import Contact from './Contact.react';

class App extends React.Component {
  constructor() {
    super();

    this.state = {
      contacts: []
    }
  }

  componentDidMount() {
    fetch('http://127.0.0.1:5000/contacts')
    .then(response => response.json())
    .then(data => {
      this.setState({ contacts: data})
    })
  }

  render() {
    return (
      <div>
        <h1> Welcome to Contacts Manager</h1>
        <ul>
          {this.state.contacts.map(contact =>
            <li key={contact.id}>
              {contact.name}, {contact.telephone}
            </li>
          )}
        </ul>
      </div>
    );
  }

}
export default App;
