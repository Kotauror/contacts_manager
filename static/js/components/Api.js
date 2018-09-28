import axios from 'axios';

class Api {

  static getContacts() {
    return axios.get('/contacts')
      .then((response) => { return response.data })
  }

  static addContact(name, telephone) {
    return axios.post('/contacts/add', {
      "name": name,
      "telephone": telephone,
    })
    .then((response) => { return response.data })
    .catch((error) => { alert("Error in adding contact") })
  }

  static deleteContact(id) {
    return axios.post('/contacts/delete', {
      "id": id
    })
    .then((response) => { return response.data })
    .catch((error) => { alert("Error in deleting contact") })
  }

  static editContact(idOfEditedContact, nameAfterEdit, telephoneAfterEdit) {
    return axios.post('/contacts/edit', {
      "idOfEditedContact": idOfEditedContact,
      "nameAfterEdit": nameAfterEdit,
      "telephoneAfterEdit": telephoneAfterEdit
    })
    .then((response) => { return response.data })
    .catch((error) => { alert("Name and telephone must be unique") })
  }
}

export default Api
