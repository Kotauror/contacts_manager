from flask import Flask, render_template, request, redirect, url_for
import sys

sys.path.insert(0, 'src')

from contacts_book import *
from contact import *

app = Flask(__name__)

contacts_book = ContactsBook()

@app.route('/contacts', methods=['GET'])
def index():
    return render_template('home.html', contacts=contacts_book.get_contacts())

@app.route('/contacts', methods=['POST'])
def addContact():
    contact = Contact(request.form)
    contacts_book.add_contact(contact)
    return redirect(url_for('index'))

@app.route('/contacts/delete/id=<string:id_to_delete>', methods=['POST'])
def deleteContact(id_to_delete):
    contacts_book.remove_contact(id_to_delete)
    return redirect(url_for('index'))

@app.route('/contacts/edit', methods=['POST'])
def findUserToEdit():
    id_to_edit = request.form['id']
    return render_template('edit.html', id_of_contact=id_to_edit)

@app.route('/contacts/edit/id=<string:id_to_edit>', methods=['POST'])
def editUser(id_to_edit):
    name = request.form['name']
    telephone = request.form['telephone']
    contacts_book.update_contact(id_to_edit, name, telephone)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
