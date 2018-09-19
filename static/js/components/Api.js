class Api {

  static getContacts() {
    return fetch('/contacts')
      .then((response) => { return response.json() })
  }

  static addContact(name, telephone) {
    return fetch('/contacts/add', {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "name": name,
        "telephone": telephone,
      })
    })
    .then((response) => { return response.json() })
  }

}

export default Api
