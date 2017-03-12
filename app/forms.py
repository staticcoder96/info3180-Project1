"""
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired

class Form(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired()])
    gender = StringField('Gender', validators=[InputRequired()])
    first_name = StringField('Firstname', validators=[InputRequired()])
    last_name = StringField('Lastname', validators=[InputRequired()])
    id = StringField('Id', validators=[InputRequired()])
    
"""    