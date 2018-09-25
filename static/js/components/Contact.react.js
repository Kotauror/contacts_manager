import React from "react";
import Api from './Api';

class Contact extends React.Component {

  render() {
    return (
      <div>
        { this.props.name }
        { this.props.telephone }
        <button onClick={(e) => this.handleDelete(e)} id='delete_button'> ❌ </button>
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
