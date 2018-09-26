import React from "react";
import Api from './Api';
import DeleteContact from './DeleteContact.react'
import EditContact from './EditContact.react'

class Contact extends React.Component {
  constructor() {
    super();

    this.state = {
      disable: true
    }
  }

  render() {
    return (
      <div>
         <input type="text" disabled={this.state.disable} defaultValue={this.props.name} />
         <input type="text" disabled={this.state.disable} defaultValue={this.props.telephone}/>
        <DeleteContact
          onClick={(e) => this.handleDelete(e)}
        />
        <EditContact
          onClick={(e) => this.handleEditClick()}
        />
      </div>
    )
  }

  handleEditClick() {
    this.setState({disable: !this.state.disable})
  }

  handleDelete(event) {
    event.preventDefault()
    Api.deleteContact(this.props.name, this.props.telephone)
    .then(contact => {
        this.props.onDeleteContact(contact)
    })
  }
}

export default Contact;
