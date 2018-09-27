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
  }

  static deleteContact(id) {
    return axios.post('/contacts/delete', {
      "id": id
    })
    .then((response) => { return response.data })
  }

  static editContact(idOfEditedContact, nameAfterEdit, telephoneAfterEdit) {
    return axios.post('/contacts/edit', {
      "idOfEditedContact": idOfEditedContact,
      "nameAfterEdit": nameAfterEdit,
      "telephoneAfterEdit": telephoneAfterEdit
    })
    .then((response) => { return response.data })
  }
}

export default Api
