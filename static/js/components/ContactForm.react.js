import React from "react";
import { Form, FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';

class ContactForm extends React.Component {

  render() {
    return (
      <div>
        <form onSubmit={(e) => this.handleSubmit(e)}>
          <FormGroup>
            <ControlLabel>Name</ControlLabel>
            <FormControl
              className='input-name'
            />
            <ControlLabel>Phone</ControlLabel>
            <FormControl
              className='input-phone'
            />
          </FormGroup>
          <Button type="submit">Submit</Button>
        </form>
      </div>
    )
  }

  handleSubmit(event) {
    console.log(event.target)
    event.preventDefault();
  }

}

export default ContactForm;
