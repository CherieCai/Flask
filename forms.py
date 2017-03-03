from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter an valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Password must be more than 6 charaters/numbers.")])
	submit = SubmitField('Sign Up')

class LoginForm(Form):
	"""docstring for ClassName"""
	companyname = StringField('Company Name', validators=[DataRequired("Please enter your company name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email('Please enter an valid email address.')])
	password = PasswordField('Password', validators= [DataRequired('Please enter your password.')])
	submit = SubmitField('Log In')


class CompForm(Form):
	"""docstring for ClassName"""
	FirmName = StringField('Company Name', validators=[DataRequired("Please enter a company name.")])
	PlanName = StringField('Plan Name', validators=[DataRequired("Please enter a plan name.")])
	IINDec = FloatField('In-network Deductible', validators=[DataRequired("Please enter a number (i.e. no dollar sign).")])
	OONDec = FloatField('Out-of-network Deductible', validators=[DataRequired("Please enter a number (i.e. no dollar sign).")])
	submit = SubmitField('submit')