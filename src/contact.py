import uuid

class Contact():

    def __init__(self, form):
        self.name = form['name']
        self.telephone = form['telephone']
        self.id = uuid.uuid4()
