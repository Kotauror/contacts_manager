import React from "react";
import { Form, FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';

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
      <div>
        <form onSubmit={(e) => this.handleSubmit(e)}>
          <FormGroup>
            <ControlLabel>Name</ControlLabel>
            <FormControl
              className='input-name'
              onChange={(e) => this.handleChangeName(e.target.value)}
            />
            <ControlLabel>Phone</ControlLabel>
            <FormControl
              className='input-phone'
              onChange={(e) => this.handleChangeTelephone(e.target.value)}
            />
          </FormGroup>
          <Button type="submit">Submit</Button>
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
    fetch('/contacts/add', {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "name": this.state.name,
        "telephone": this.state.telephone,
      })
    }).then(response => response.json())
      .then(contact => {
        this.props.onAddContact(contact)
      })
    event.preventDefault()
  }
}

export default ContactForm;
