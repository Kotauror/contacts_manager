from flask import Flask, render_template, request
import sys

sys.path.insert(0, 'src')

from contacts_book import *
from contact import * 

app = Flask(__name__)

contacts_book = ContactsBook()

@app.route('/contacts', methods=['GET'])
def index():
    return render_template('home.html', contacts = contacts_book.get_contacts())

@app.route('/contacts', methods=['POST'])
def addContact():
    contact = Contact(request.form)
    contacts_book.add_contact(contact)
    return render_template('home.html', contacts = contacts_book.get_contacts())

if __name__ == '__main__':
    app.run(debug=True)
