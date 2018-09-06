from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.insert(0, 'src')
from contact import *
from settings import app, db

@app.route('/contacts', methods=['GET'])
def index():
    contacts = Contact.query.all()
    messages = request.args.get('messages')
    return render_template('home.html', contacts=contacts, messages=messages)

@app.route('/contacts', methods=['POST'])
def addContact():
    try:
        contact = Contact(request.form['name'], request.form['telephone'])
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('index', messages="Contact added successfully"))
    except:
        return redirect(url_for('index', messages="Error: either name or telephone are already in the database"))

@app.route('/contacts/delete/id=<string:id_to_delete>', methods=['POST'])
def deleteContact(id_to_delete):
    try:
        contact_to_delete = Contact.query.filter_by(id=id_to_delete).first()
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect(url_for('index', messages="Contact deleted successfully"))
    except:
        return redirect(url_for('index', messages="Error in deleting"))

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
        return redirect(url_for('index', messages="Contact edited successfully"))
    except:
        return redirect(url_for('index', messages="Error in editing"))

if __name__ == '__main__':
    app.run(debug=True)
