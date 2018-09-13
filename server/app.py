from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from src.messages import *
from settings import app, db
from src.contacts_book import ContactsBook

contacts_book = ContactsBook()

@app.route('/', methods=['GET'])
def testRoute():
    return render_template("index.html")

@app.route('/contacts', methods=['GET'])
def index():
    # contacts = contacts_book.get_contacts()
    # message = request.args.get('message')
    # return render_template('home.html', contacts=contacts, message=message)
    contacts = contacts_book.get_contacts_as_jsons()
    return json.dumps(contacts)

@app.route('/contacts', methods=['POST'])
def addContact():
    try:
        contacts_book.add_contact(request.form['name'], request.form['telephone'])
        return redirect(url_for('index', message=Messages.ADD_SUCCESS.value))
    except:
        return redirect(url_for('index', message=Messages.ADD_ERROR.value))

@app.route('/contacts/delete/id=<string:id_to_delete>', methods=['POST'])
def deleteContact(id_to_delete):
    try:
        contacts_book.delete_contact_by_id(id_to_delete)
        return redirect(url_for('index', message=Messages.DELETE_SUCCESS.value))
    except:
        return redirect(url_for('index', message=Messages.DELETE_ERROR.value))

@app.route('/contacts/edit', methods=['POST'])
def findUserToEdit():
    id_to_edit = request.form['id']
    return render_template('edit.html', id_of_contact=id_to_edit)

@app.route('/contacts/edit/id=<string:id_to_edit>', methods=['POST'])
def editUser(id_to_edit):
    try:
        contacts_book.edit_contact_by_id(id_to_edit, request.form['name'], request.form['telephone'])
        return redirect(url_for('index', message=Messages.EDIT_SUCCESS.value))
    except:
        return redirect(url_for('index', message=Messages.EDIT_ERROR.value))

if __name__ == '__main__':
    app.run(debug=True)
