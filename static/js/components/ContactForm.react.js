import Api from './Api';
import React from "react";
import { Form, FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';
import '../../styles/contactFormComponent.css'

class ContactForm extends React.Component {
  constructor() {
    super();

    this.state = {
      name: "",
      telephone: "",
    }
  }

  render() {
    return (
      <div className="contact-form">
        <form onSubmit={(e) => this.handleSubmit(e)}>
          <FormGroup>
            <ControlLabel>Name: </ControlLabel>
            <FormControl
              className='input-name'
              onChange={(e) => this.handleChangeName(e.target.value)}
            />
          <ControlLabel>Phone: </ControlLabel>
            <FormControl
              className='input-phone'
              onChange={(e) => this.handleChangeTelephone(e.target.value)}
            />
          </FormGroup>
          <Button className='btn-add' type="submit">Submit</Button>
        </form>
      </div>
    )
  }

  handleChangeName(name) {
    this.setState({name});
  }

  handleChangeTelephone(telephone) {
    this.setState({telephone});
  }

  handleSubmit(event) {
    event.preventDefault()
    Api.addContact(this.state.name, this.state.telephone)
    .then(contact => {
        this.props.onAddContact(contact)
      })
  }
}

export default ContactForm;
