from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
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
    req = request.get_json()
    contact = contacts_book.add_contact(req['name'], req['telephone'])
    return contacts_book.contact_to_json(contact)

@app.route('/contacts/delete', methods=['POST'])
def deleteContact():
    req = request.get_json()
    contact = contacts_book.delete_contact(req['id'])
    return contacts_book.contact_to_json(contact)

@app.route('/contacts/edit', methods=['POST'])
def editttContact():
    req = request.get_json()
    infoAboutEdit = contacts_book.edit_contact(req['idOfEditedContact'], req['nameAfterEdit'], req['telephoneAfterEdit'])
    return json.dumps(infoAboutEdit)

if __name__ == '__main__':
    app.run(debug=True)
