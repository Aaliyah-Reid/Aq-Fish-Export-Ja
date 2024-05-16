from . import db
from werkzeug.security import generate_password_hash
class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self,username,password,is_admin):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.is_admin = is_admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
    
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
        self.availability = availability
        self.photo_filename = photo_filename 

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<Fish %r>' % (self.name)
    

