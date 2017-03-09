from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, CompModel
from forms import LoginForm, CompForm
import pyodbc

import urllib

app = Flask(__name__, static_url_path="/static", static_folder="static")


server = 'btrwebsitedata.database.windows.net'
database = 'WebsiteData'
username = 'btr.helpdesk'
password = 'Benchmark123'
port = '1433'
db_name = 'WebsiteData'
driver = 'ODBC Driver 13 for SQL Server'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://{}:{}@{}:{}/{}?driver={}".format(
    username, password, server, port, db_name, driver)

# app.config['SQLALCHEMY_DATABASE_URI'] =
# 'postgresql://localhost/learningflask'

db.init_app(app)
with app.app_context():
    user = User.query.filter_by(email="test@dayblink.com").first()
    assert user.companyname == 'BTR'


# Configure the user sign up form using CSRF
# Create an instance of secrete to generate a secure form in Flask
app.secret_key = "development-key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/home", methods=['GET', 'POST'])
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('home.html')


@app.route('/login', methods=["GET", 'POST'])
def login():
    if 'email' in session:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == "POST":
        if not form.validate():
            print("form not validated")
            return render_template("login.html", form=form)
        else:
            companyname = form.companyname.data
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()

            if user is not None and user.check_password(password) and user.check_companyname(companyname):
                session['email'] = form.email.data
                print('going to home page')
                return redirect(url_for('home'))
            else:
                print('authentication failed.')
                return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route("/compchoose")
def compchoose():
    if 'email' not in session:
        return redirect(url_for('login'))
    else:
        return render_template("compchoose.html")


@app.route("/compchoose1")
def compchoose1():
    return render_template("compchoose1.html")


@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template("logout.html")


@app.route('/compenter', methods=["GET", 'POST'])
def compenter():
	form = CompForm()
	if request.method == "POST":
		if not form.validate():
			print('invalid form')
			return render_template('compenter.html', form=form)
		else:
			newform = CompModel(form.CompanyName.data, form.CompanySize.data, form.CompanyState.data, form.WaitRule.data, form.FundingMethod.data, form.BenefitPlan.data, form.MonthlyPremium_Single.data, form.MonthlyPremium_Family.data, form.EEMonthly_Single.data, form.ERMonthly_Single.data, form.EEMonthly_Family.data, form.ERMonthly_Family.data)
	    	db.session.add(newform)
	    	db.session.commit()
	    	print('entered data')
	    	return redirect(url_for('compenter'))

	elif request.method == 'GET':
		return render_template('compenter.html', form=form)

if __name__ == "__main__":
    app.run()
