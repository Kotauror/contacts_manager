class Api {

  static getContacts() {
    return fetch('/contacts')
      .then((response) => {
        if(response.ok) {
          return response.json()
        }
      })
  }

}

export default Api
