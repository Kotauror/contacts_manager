from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.insert(0, 'src')
from contact import *
from settings import app, db

@app.route('/contacts', methods=['GET'])
def index():
    contacts = Contact.query.all()
    return render_template('home.html', contacts=contacts)

@app.route('/contacts', methods=['POST'])
def addContact():
    contact = Contact(request.form['name'], request.form['telephone'])
    db.session.add(contact)
    db.session.commit()
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
