from flask_wtf import Form
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name',validators=[DataRequired("Please enter your First Name.")])
	last_name = StringField('Last Name',validators=[DataRequired("Please enter your Last Name.")])
	email = StringField('Email',validators=[DataRequired("Please enter your Email."),Email("Please enter your Email Address.")])
	password = PasswordField('Password',validators=[DataRequired("Please enter your Password."), Length(min=8, message="Password must be 8 characters minimum")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email',validators=[DataRequired("Please enter your Email."),Email("Please enter your Email Address.")])
	password = PasswordField('Password',validators=[DataRequired("Please enter your Password.")])
	submit = SubmitField('Sign in')

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Please enter an address.")])
	submit = SubmitField("Search")