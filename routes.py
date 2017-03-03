from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm, CompForm
import pyodbc

import urllib

app = Flask(__name__)


'''

server = 'btrwebsitedata.database.windows.net'
database = 'WebsiteData'
username = 'btr.helpdesk'
password = 'Benchmark123'
port = '1433'
db_name = 'WebsiteData'
driver= 'ODBC Driver 13 for SQL Server'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://{}:{}@{}:{}/{}?driver={}".format(
	username, password, server, port, db_name, driver) 

'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'  
	
db.init_app(app)
'''with app.app_context():
	user = User.query.filter_by(email="test@dayblink.com").first()
	print(user.companyname)
'''

# Configure the user sign up form using CSRF 
# Create an instance of secrete to generate a secure form in Flask
app.secret_key = "development-key"


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")


#don't know between get and POST
@app.route("/signup", methods=['GET','POST'])
def signup():
	#if 'email' in session:
		#return redirect(url_for('home'))

	form = SignupForm()
	if request.method=='POST':
		if form.validate()==False:
			return render_template('signup.html',form=form)
		else:
			#newuser= User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			#db.session.add(newuser)
			#db.session.commit()

			#session['email'] = newuser.email
			return redirect(url_for('home'))

	elif request.method=="GET":
		return render_template('signup.html', form=form)

@app.route("/home", methods=['GET','POST'])
def home():
	#if 'email' not in session:
		#return redirect(url_for ('login'))
	#else:
	
	form = CompForm()
	if request.method=='POST':
		if form.validate()==False:
			return render_template('home.html',form=form)
		else:
			#newuser= User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			#db.session.add(newuser)
			#db.session.commit()

			#session['email'] = newuser.email
			return redirect(url_for('home'))

	elif request.method=="GET":
		return render_template('home.html', form=form)
	'''
		form = AddressForm()
		if request.method == "POST":
			if form.validate() == False:
				redirect(url_for('home'))

		elif request.method == "GET":
			return render_template('home.html')
			'''

@app.route('/login', methods=["GET", 'POST'])
def login():
	#if 'email' in session:
		#return redirect(url_for('home'))

	form = LoginForm()
	if  request.method =="POST":
		if form.validate() ==False:
			return render_template("login.html", form=form)
		else:
			return redirect(url_for('home'))
		'''if form.validate() ==False:
			return render_template("login.html", form=form)
		else:
			email = form.email.data
			password = form.password.data
			user = User.query.filter_by(email=email).first()

			if user is not None and user.check_password(password):
				session['email'] = form.email.data
			else:
				return redirect(url_for('login'))
		'''	
	elif request.method=='GET':
		return render_template('login.html', form=form)

@app.route("/compchoose")
def compchoose():
  return render_template("compchoose.html")

@app.route('/logout')
def logout():
	#session.pop('email', None)
	return render_template("logout.html")



if __name__ == "__main__":
  app.run()