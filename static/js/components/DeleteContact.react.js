import React from "react";

class DeleteContact extends React.Component {

  render() {
    return (
        <button onClick={(e) => this.props.onClick(e)} id='delete_button'> ❌ </button>
    )
  }
}

export default DeleteContact;
