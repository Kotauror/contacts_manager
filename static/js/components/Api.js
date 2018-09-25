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
}

export default Api
