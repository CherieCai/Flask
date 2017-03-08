from flask_wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SubmitField, FloatField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from wtforms import validators
'''
class SignupForm(Form):
	first_name = StringField('First name', validators=[
	                         DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[
	                        DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired(
	    "Please enter your email address."), Email("Please enter an valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(
	    min=6, message="Password must be more than 6 charaters/numbers.")])
	submit = SubmitField('Sign Up')
'''


class LoginForm(Form):
    companyname = StringField('Company Name', validators=[
                              DataRequired("Please enter your company name.")])
    email = StringField('Email', validators=[DataRequired(
        "Please enter your email address."), Email('Please enter an valid email address.')])
    password = PasswordField('Password', validators=[
                             DataRequired('Please enter your password.')])
    submit = SubmitField('Log In')


class CompForm(Form):
	# docstring for ClassName
	# PlanYear = IntegerField('Plan Year', validators.Length(min=2016, message='Please enter a plan year that is after 2016.'))
    # TODO: Need to Concatinates the start and finish Date
    # start date, end date need to fix!!

    CompanyName = StringField('Company Name')
    CompanySize = IntegerField("Company Size", validators=[
    	NumberRange(min=0, message='Please enter a number that is larger than 0.')])
    Statelist = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'),
                 ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IO', 'IO'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'),
                 ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'),
                 ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'),
                 ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]
    CompanyState = SelectField('Comapny State', choices=Statelist)
    # SIC = SelectField('Industry/SIC code', choices = SIClist)

    '''
    WaitRule = RadioField('Gender', choices=[(
        'Immediately following', 'Immediately following'), ('First of month following', 'First of month following')])

    Funding = StringField('Waiting Days')
    WaitDays = SelectField('Funding Method', choices=[(
        'Immediately following', 'Immediately following'), ('First of month following', 'First of month following')])

    BenefitType = StringField('Type of Plan (e.g. Medical, Dental, Vision...')
    BenefitPlan = StringField('Plan Name')

    MonthlyPremium = FloatField('Total Monthly Premium')
    EEMonthly = FloatField('Monthly Premium Contributed by Employee')
    ERMonthly = FloatField('Monthly Premium Contributed by Employer')
	'''
    '''Carrier = StringField("Carrier Name")
	In_Ded_Single = FloatField('In-network Deductible for Single Coverage')
	In_Ded_Family = FloatField('In-network Deductible for Family Coverage')
	# In_PerInsuredFlag_Family
	Out_Ded_Single = FloatField('Out-of-network Deductible for Single coverage')
	Out_Ded_Family = FloatField('Out-of-network Deductible for Family coverage')
	# Out_PerInsuredFlag_Family
	In_OOP_Single = FloatField('In-network out-of-pocket maximum for Single coverage')
	In_OOP_Family = FloatField('In-network out-of-pocket maximum for Family coverage')
	Out_OOP_Single = FloatField('Out-of-network out-of-pocket maximum for Single coverage')
	Out_OOP_Family = FloatField('Out-of-network out-of-pocket maximum for Family coverage')
	In_Copay_PCP = FloatField('In-network Primary Care Pysician Copay')
	In_Coins_PCP = FloatField('In-network Primary Care Pysician Co-insurance')
	In_Copay_SCP = FloatField('In-network Specialist Care Pysician Copay')
	In_Coins_SCP = FloatField('In-network Specialist Care Pysician Co-insurance')
	In_Copay_Lab = FloatField('In-network Lab Copay')
	In_Coins_Lab = FloatField('In-network Lab Co-insurance')
	In_Copay_Xray = FloatField('In-network X-ray Copay')
	In_Coins_Xray = FloatField('In-network X-ray Co-insurance')
	Out_Copay_PCP = FloatField('Out-of-network Primary Care Pysician Copay')
	Out_Coins_PCP = FloatField('Out-of-network Primary Care Pysician Co-insurance')
	Out_Copay_SCP = FloatField('Out-of-network Specialist Care Pysician Copay')
	Out_Coins_SCP = FloatField('Out-of-network Specialist Care Pysician Co-insurance')
	Out_Copay_Lab = FloatField('Out-of-network Lab Copay')
	Out_Coins_Lab = FloatField('Out-of-network Lab Co-insurance')
	Out_Copay_Xray = FloatField('Out-of-network X-ray Copay')
	Out_Coins_Xray = FloatField('Out-of-network X-ray Co-insurance')

	# Inf_Infertility
	Rx_Tiers = IntegerField('Number of tiers for Rx Benefits')
	Rx_Copay_PrefGeneric = FloatField('Retail Copay for Preferred Generic Rx')
	Rx_Coins_PrefGeneric = FloatField('Retail Co-insurance for Preferred Generic Rx')
	Rx_Copay_NonPrefGeneric = FloatField('Retail Copay for Non-preferred Generic Rx')
	Rx_Coins_NonPrefGeneric= FloatField('Retail Co-insurance for Non-Preferred Generic Rx')
	Rx_Copay_PrefBrand = FloatField('Retail Copay for Preferred Brand Rx')
	Rx_Coins_PrefBrand= FloatField('Retail Co-insurance for Preferred Brand Rx')
	Rx_Copay_NonPrefBrand= FloatField('Retail Copay for Non-preferred Brand Rx')
	Rx_Coins_NonPrefBrand= FloatField('Retail Co-insurance for Non-referred Generic Rx')
	Rx_Copay_Specialty= FloatField('Retail Copay for Speciality Rx')
	Rx_Coins_Specialty= FloatField('Retail Co-insurance for Speciality Rx')
	Rx_Copay_Other= FloatField('Retail Copay for Rx in other tiers')
	Rx_Coins_Other = FloatField('Retail Co-insurance for Rx in other tiers')
	Rx_MailOrderMultiple = FloatField('Rx Mail Order Plan desgin (x1, x2, x2.5, others, None)')
	# Rx_SubjectToMajorDed
	# Rx_SeparateRxDed 
	# Rx_SeparateInjectibesDed
	# Rx_Exclude_DispenseAsWritten
	IN_Copay_ER = FloatField('In-network Emergency Room Copay')
	In_Coins_ER= FloatField('In-network Emergency Room Co-insurance')
	IN_Copay_UC= FloatField('In-network Urgency Care Copay')
	In_Coins_UC= FloatField('In-network Urgency Care Co-insurance')
	IN_Copay_InpatientHosp = FloatField('In-network In-patient Hospitalization Copay')
	In_Coins_InpatientHosp= FloatField('In-network In-patient Hospitalization Co-insurance')
	IN_Copay_OutSurgery = FloatField('In-network Out-patient Surgery Copay')
	In_Coins_OutSurgery= FloatField('In-network Out-patient Surgery Co-insurance')
	Out_Copay_ER = FloatField('Out-of-network Emergency Room Copay')
	Out_Coins_ER= FloatField('Out-of-network Emergency Room Co-insurance')
	Out_Copay_UC= FloatField('Out-of-network Urgency Care Copay')
	Out_Coins_UC= FloatField('Out-of-network Urgency Care Co-insurance')
	Out_Copay_InpatientHosp = FloatField('Out-of-network In-patient Hospitalization Copay')
	Out_Coins_InpatientHosp= FloatField('Out-of-network In-patient Hospitalization Co-insurance')
	Out_Copay_OutSurgery = FloatField('Out-of-network Out-patient Surgery Copay')
	Out_Coins_OutSurgery= FloatField('Out-of-network Out-patient Surgery Co-insurance')
'''
    submit = SubmitField('submit')
