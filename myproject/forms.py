from flask_wtf import FlaskForm
from wtforms import StringField,TextField,TextAreaField,SubmitField, PasswordField, HiddenField, BooleanField, SelectField, FileField, DateField, DateTimeField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length
from myproject import db
from wtforms.fields.html5 import DateField

class ShortForm(FlaskForm):
    url = StringField('Url', render_kw={"placeholder": "URL"})
    submit = SubmitField('Go')