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

  static deleteContact(name, telephone) {
    return axios.post('/contacts/delete', {
      "name": name,
      "telephone": telephone,
    })
    .then((response) => { return response.data })
  }

  static editContact(oldName, oldPhone, newName, newPhone) {
    return axios.post('/contacts/edit', {
      "oldContactName": oldName,
      "oldContactTelephone": oldPhone,
      "newContactName": newName,
      "newContactTelephone": newPhone
    })
    .then((response) => { return response.data })
  }


}

export default Api
