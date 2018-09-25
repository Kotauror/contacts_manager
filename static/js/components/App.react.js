import React, { Component } from "react";
import Contact from './Contact.react';
import ContactForm from './ContactForm.react';
import Api from './Api';
import axios from 'axios';


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

  removeContact(contactToRemove) {
    const { contacts } = this.state
    var result = contacts.filter(contact => this._areContactsEqual(contact, contactToRemove))
    this.setState({ contacts: result })
  }

  _areContactsEqual(contact1, contact2) {
    (contact1.name.localeCompare(contact2.name)) &&
    (contact1.telephone.localeCompare(contact2.telephone))
  }
}

export default App;
