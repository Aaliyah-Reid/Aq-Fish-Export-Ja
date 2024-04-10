from . import db


class Fish(db.Model):

    __tablename__ = 'fishes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    breed = db.Column(db.String(80))
    description = db.Column(db.String(250))
    availability = db.Column(db.String(80))
    photo_filename = db.Column(db.String(255))

    def __init__(self, name, breed, description, availability , photo_filename):
        self.name = name
        self.breed = breed
        self.description = description
        self.availabilty = availability
        self.photo_filename = photo_filename

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<Property %r>' % (self.title)