from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from src.messages import *
from settings import app, db
from src.contacts_book import ContactsBook

contacts_book = ContactsBook()

@app.route('/', methods=['GET'])
def homeRoute():
    return render_template("index.html")

@app.route('/contacts', methods=['GET'])
def index():
    return contacts_book.get_contacts_as_jsons()

@app.route('/contacts/add', methods=['POST'])
def addContact():
    content_of_request = request.get_json()
    contact = contacts_book.add_contact(content_of_request['name'], content_of_request['telephone'])
    return contacts_book.contact_to_json(contact)

@app.route('/contacts/delete', methods=['POST'])
def deleteContact():
    content_of_request = request.get_json()
    contact = contacts_book.delete_contact_by_name(content_of_request['name'])
    return contacts_book.contact_to_json(contact)

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
