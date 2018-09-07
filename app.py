from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
from src.messages import *
from settings import app, db
from src.contact import *
from src.contacts_book import *

contacts_book = ContactsBook()

@app.route('/contacts', methods=['GET'])
def index():
    contacts = Contact.query.all()
    message = request.args.get('message')
    return render_template('home.html', contacts=contacts, message=message)

@app.route('/contacts', methods=['POST'])
def addContact():
    try:
        contact = Contact(request.form['name'], request.form['telephone'])
        contacts_book.add_contact(contact)
        return redirect(url_for('index', message=Messages.ADD_SUCCESS.value))
    except:
        return redirect(url_for('index', message=Messages.ADD_ERROR.value))

@app.route('/contacts/delete/id=<string:id_to_delete>', methods=['POST'])
def deleteContact(id_to_delete):
    try:
        contact_to_delete = Contact.query.filter_by(id=id_to_delete).first()
        contacts_book.delete_contact(contact_to_delete)
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
        contact_to_update = Contact.query.filter_by(id=id_to_edit).first()
        contact_to_update.name = request.form['name']
        contact_to_update.telephone = request.form['telephone']
        db.session.commit()
        return redirect(url_for('index', message=Messages.EDIT_SUCCESS.value))
    except:
        return redirect(url_for('index', message=Messages.EDIT_ERROR.value))

if __name__ == '__main__':
    app.run(debug=True)
