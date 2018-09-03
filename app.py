from flask import Flask, render_template, request, redirect, url_for
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
    return redirect(url_for('index'))

@app.route('/contacts/delete', methods=['POST'])
def deleteContact():
    id_to_remove = request.form['id']
    contacts_book.remove_contact(id_to_remove)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
