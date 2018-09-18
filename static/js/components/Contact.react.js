import React from "react";

class Contact extends React.Component {

  render() {
    return (
      <div>
        { this.props.name }
        { this.props.telephone }
      </div>
    )
  }
}

export default Contact;
