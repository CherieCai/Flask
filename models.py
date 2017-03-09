from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

'''
Create a table in Python
'''
'''
Create a init function
'''
'''
encrpt password
'''


class User(db.Model):
    __tablename__ = 'UserLogIn'
    uid = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwshash = db.Column(db.String(54))

    def __init__(self, companyname, email, password):
        self.companyname = companyname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwshash = generate_password_hash(password)

    def check_password(self, password):
        return self.pwshash == password

    def check_companyname(self, companyname):
        return self.companyname == companyname


class CompModel(db.Model):
    __tablename__ = 'PlanDetailEntry'
    ID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(100))
    CompanySize = db.Column(db.Integer)
    CompanyState = db.Column(db.String(2))
    WaitRule = db.Column(db.String(100))
    # WaitDays = db.Column(db.Float)
    BenefitPlan = db.Column(db.String(250))
    FundingMethod = db.Column(db.String(100))
    MonthlyPremium_Single = db.Column(db.Float)
    MonthlyPremium_Family = db.Column(db.Float)
    EEMonthly_Single = db.Column(db.Float)
    ERMonthly_Single = db.Column(db.Float)
    EEMonthly_Family = db.Column(db.Float)
    ERMonthly_Family = db.Column(db.Float)

    def __init__(self, CompanyName, CompanySize, CompanyState, WaitRule, FundingMethod, BenefitPlan, MonthlyPremium_Single, MonthlyPremium_Family, EEMonthly_Single, ERMonthly_Single, EEMonthly_Family, ERMonthly_Family):
        self.CompanyName = CompanyName
        self.CompanySize = CompanySize
        self.CompanyState = CompanyState
        self.WaitRule = WaitRule
        # self.WaitDays = WaitDays
        self.FundingMethod = FundingMethod
        self.BenefitPlan = BenefitPlan
        self.MonthlyPremium_Single = float(MonthlyPremium_Single)
        self.MonthlyPremium_Family = float(MonthlyPremium_Family)
        self.EEMonthly_Single = float(EEMonthly_Single)
        self.ERMonthly_Single = float(ERMonthly_Single)
        self.EEMonthly_Family = float(EEMonthly_Family)
        self.ERMonthly_Family = float(ERMonthly_Family)
