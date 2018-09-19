import React, { Component } from "react";
import Contact from './Contact.react';
import ContactForm from './ContactForm.react';
import Api from './Api';


class App extends React.Component {
  constructor() {
    super();

    this.state = {
      contacts: []
    }
  }

  componentDidMount() {
    Api.getContacts().then(data => { this.setState({ contacts: data}) })
  }

  render() {
    return (
      <div>
        <h1> Welcome to Contacts Manager</h1>
        <ContactForm
          onAddContact={(c) => this.addContact(c)}
        />
        <div className="contacts-list">
          { this.state.contacts.map(contact => {
              return (
                <Contact
                  key={contact.id}
                  name={contact.name}
                  id={contact.id}
                  telephone={contact.telephone}
                />
              )
            }) }
        </div>
      </div>
    )
  }

  addContact(contact) {
    const { contacts } = this.state
    contacts.push(contact)
    this.setState({ contacts })
  }

}

export default App;
