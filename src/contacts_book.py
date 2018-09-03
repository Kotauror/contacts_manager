class ContactsBook():

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

    def remove_contact(self, contact_id_to_remove):
        for contact in self.contacts:
            if str(contact.id) == contact_id_to_remove:
                self.contacts.remove(contact)

    def update_contact(self, contact_id_to_change, name, telephone):
        for contact in self.contacts:
            if str(contact.id) == contact_id_to_change:
                contact.name = name
                contact.telephone = telephone
