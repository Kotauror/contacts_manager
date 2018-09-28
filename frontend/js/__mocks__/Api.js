import axios from 'axios';

class Api {

  static getContacts() {
    return new Promise(function(resolve, reject) {
      resolve([{
        name: "Justyna",
               telephone: "111111",
               id: 110
      },
      {
        name: "kosia",
               telephone: "222",
               id: 110
      }
      ])
    })
  }

  static addContact(name, telephone) {
  }
}

export default Api
