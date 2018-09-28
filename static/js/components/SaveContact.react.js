import React from "react";
import '../../styles/saveContactComponent.css'

class SaveContact extends React.Component {

  render() {
    return (
        <button onClick={(e) => this.props.onClick(e)} id='save_button'> 💾  </button>
    )
  }
}

export default SaveContact;
