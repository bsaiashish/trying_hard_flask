from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,  Length


class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")
