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
           id="nameInput"
         />
         <input
           type="text"
           disabled={this.state.disable}
           defaultValue={this.props.telephone}
           onChange={(e) => this.handleChangeTelephone(e.target.value)}
           id="telephoneInput"
          />
        <EditContact
          onClick={(e) => this.handleEdit()}
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

  handleEdit() {
    this.setState({disable: !this.state.disable})
  }

  handleSave(e) {
    this.setState({disable: true})
    var idOfEditedContact = this.props.id
    var nameAfterEdit = this.getNameAfterEdit();
    var telephoneAfterEdit = this.getTelephoneAfterEdit();
    Api.editContact(idOfEditedContact, nameAfterEdit, telephoneAfterEdit)
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

  getNameAfterEdit() {
    return (this.state.newName.length == 0 ? this.props.name : this.state.newName)
  }

  getTelephoneAfterEdit() {
    return (this.state.newTelephone.length == 0 ? this.props.telephone : this.state.newTelephone)
  }
}

export default Contact;
