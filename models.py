from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

#create an instance called db in SQLAlchemy class

'''
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

dialect+driver://username:password@host:port/database
'''



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
  uid = db.Column(db.Integer, primary_key = True)
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