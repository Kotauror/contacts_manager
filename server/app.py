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
def editttContact():
    req = request.get_json()
    editInformation = contacts_book.edit_contact_by_name(req['oldContactName'], req['newContactName'], req['newContactTelephone'])
    return json.dumps(editInformation)

if __name__ == '__main__':
    app.run(debug=True)
