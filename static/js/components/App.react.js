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
    fetch('/contacts')
      .then(response => response.json())
      .then(data => {
        this.setState({ contacts: data})
      })
  }

  render() {
    return (
      <div>
        <h1> Welcome to Contacts Manager</h1>
        <div className="contacts-list">
          {
            this.state.contacts.map(contact => {
              return (
                <Contact
                  key={contact.id}
                  name={contact.name}
                  telephone={contact.telephone}
                />
              )
            })
          }
        </div>
      </div>
    )
  }
}
export default App;
