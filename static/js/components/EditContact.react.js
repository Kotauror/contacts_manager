import React from "react";

class EditContact extends React.Component {

  render() {
    return (
      <button onClick={(e) => this.props.onClick(e)} id='edit_button'> ✍ </button>
    )
  }
}

export default EditContact;
