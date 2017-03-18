from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField
from wtforms.validators import InputRequired

class Form(FlaskForm):
    age = IntegerField('age', validators=[InputRequired()])
    gender = SelectField(label='gender',choices=[("Male","Male"),("Female","Female")])
    fname = StringField('fname', validators=[InputRequired()])
    lname = StringField('lname', validators=[InputRequired()])
    userid = StringField('Id', validators=[InputRequired()])
    bio = StringField('bio',validators=[InputRequired()])
    
    