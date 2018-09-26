import React from "react";
import Api from './Api';
import DeleteContact from './DeleteContact.react'

class Contact extends React.Component {

  render() {
    return (
      <div>
        { this.props.name }, { this.props.telephone }
        <DeleteContact
          onClick={(e) => this.handleDelete(e)}
        />
      </div>
    )
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
