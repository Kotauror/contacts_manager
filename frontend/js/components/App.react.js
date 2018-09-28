import axios from 'axios';
import Api from '../Api';
import Contact from './Contact.react';
import ContactForm from './ContactForm.react';
import React, { Component } from "react";
import '../../styles/appComponent.css'

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
        <h1> Contacts Manager</h1>
        <ContactForm
          onAddContact={(contact) => this.addContact(contact)}
        />
        <div className="contacts-list">
          { this.state.contacts.map((contact, index) => {
              return (
                <div className="single-contact" key={index}>
                  <p1>{index + 1}.</p1>
                  <Contact
                    key={contact.id}
                    name={contact.name}
                    id={contact.id}
                    telephone={contact.telephone}
                    onDeleteContact={(c) => this.deleteContact(c)}
                    onEditContact={(editInformation) => this.editContact(editInformation)}
                  />
              </div>
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
        contact.name = editInformation.nameAfterEdit,
        contact.telephone = editInformation.telephoneAfterEdit
      }
    })
    this.setState({ contacts })
  }
}

export default App;
