import axios from 'axios';
import Api from './Api';
import Contact from './Contact.react';
import ContactForm from './ContactForm.react';
import React, { Component } from "react";

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
          onAddContact={(contact) => this.addContact(contact)}
        />
        <div className="contacts-list">
          { this.state.contacts.map(contact => {
              return (
                <Contact
                  key={contact.id}
                  name={contact.name}
                  id={contact.id}
                  telephone={contact.telephone}
                  onDeleteContact={(c) => this.deleteContact(c)}
                  onEditContact={(editInformation) => this.editContact(editInformation)}
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

  deleteContact(contactToRemove) {
    const { contacts } = this.state
    var result = contacts.filter(contact => !(contact.name == contactToRemove.name))
    this.setState({ contacts: result })
  }

  editContact(editInformation) {
    const { contacts } = this.state
    contacts.map(contact => {
      if (contact.id == editInformation.idOfEditedContact) {
        contact.name = editInformation.newName,
        contact.telephone = editInformation.newTelephone
      }
    })
    this.setState({ contacts })
  }
}

export default App;
