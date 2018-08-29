from flask import Flask, render_template, request
import sys

sys.path.insert(0, 'src')

from contacts_book import *
from contact import * 

app = Flask(__name__)

contacts_book = ContactsBook()
contact = Contact("Justyna", 123)
contacts_book.add_contact(contact)

@app.route('/')
def index():
    return render_template('home.html', contacts = contacts_book.get_contacts())

@app.route('/add', methods=['POST'])
def addContact():
    name = request.form['name']
    telephone = request.form['telephone']
    contact = Contact(name, telephone)
    contacts_book.add_contact(contact)
    return render_template('home.html', contacts = contacts_book.get_contacts(), message = "Success")

if __name__ == '__main__':
    app.run(debug=True)
