import axios from 'axios';

class Api {

  static getContacts() {
    return new Promise(function(resolve, reject) {
      resolve([{
        name: "Justyna",
               telephone: "111111",
               id: 1
      },
      {
        name: "kosia",
               telephone: "222",
               id: 2
      }
      ])
    })
  }

  static addContact(name, telephone) {
    return new Promise(function(resolve, reject) {
      resolve({
        name: "Kosinka",
               telephone: "5555",
               id: 3
        })
    })
  }
}

export default Api
