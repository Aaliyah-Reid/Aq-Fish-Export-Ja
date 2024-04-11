from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, PasswordField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Email
from flask_wtf.file import FileAllowed
from flask_wtf.csrf import CSRFProtect


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    fish = StringField('Fish Interested In (optional)') 
    message = TextAreaField('Message', validators=[DataRequired()])
    subscribe = BooleanField('I want to be notified about new stock.')


class AddFishForm(FlaskForm):
    name = StringField('Fish Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    breed = StringField('Fish Breed', validators=[InputRequired()]) 
    availability = SelectField('Availability', choices=[('available', 'Available'), ('unavailable', 'Unavailable')], validators=[InputRequired()])
    photo = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])




