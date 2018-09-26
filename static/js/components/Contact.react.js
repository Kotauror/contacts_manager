import React from "react";
import Api from './Api';
import DeleteContact from './DeleteContact.react'
import EditContact from './EditContact.react'
import SaveContact from './SaveContact.react'

class Contact extends React.Component {
  constructor() {
    super();

    this.state = {
      disable: true,
      newName: "",
      newTelephone: ""
    }
  }

  render() {
    return (
      <div>
         <input
           type="text"
           disabled={this.state.disable}
           defaultValue={this.props.name}
           onChange={(e) => this.handleChangeName(e.target.value)}
         />
         <input
           type="text"
           disabled={this.state.disable}
           defaultValue={this.props.telephone}
           onChange={(e) => this.handleChangeTelephone(e.target.value)}
          />
        <EditContact
          onClick={(e) => this.handleEditClick()}
        />
        <SaveContact
          onClick={(e) => this.handleSave(e)}
        />
        <DeleteContact
          onClick={(e) => this.handleDelete(e)}
        />
      </div>
    )
  }

  handleChangeName(newName) {
    this.setState({newName});
  }

  handleChangeTelephone(newTelephone) {
    this.setState({newTelephone});
  }

  handleEditClick() {
    this.setState({disable: !this.state.disable})
  }

  handleSave(e) {
    this.setState({disable: true})
    var oldContact = {
      name: this.props.name,
      telephone: this.props.telephone
    }
    var newContact = {
      name: this.state.newName,
      telephone: this.state.newTelephone
    }

    Api.editContact(oldContact, newContact)
    .then(editInformation => {
      this.props.onEditContact(editInformation)
    })
    
    this.clearDataInState()
  }

  handleDelete(e) {
    Api.deleteContact(this.props.name, this.props.telephone)
    .then(contact => {
        this.props.onDeleteContact(contact)
    })
  }

  clearDataInState() {
    this.state.newName = ""
    this.state.newTelephone = ""
  }
}

export default Contact;
