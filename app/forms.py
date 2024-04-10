from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileAllowed
from flask_wtf.csrf import CSRFProtect

class addFishForm(FlaskForm):
    name = StringField('Fish Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    breed = StringField('Fish Breed', validators=[InputRequired()]) 
    availability = SelectField('Availability', choices=[('available', 'Available'), ('unavailable', 'Unavailable')], validators=[InputRequired()])
    photo = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])




