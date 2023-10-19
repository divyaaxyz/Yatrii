import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/yatri_signup'
db.init_app(app)

class Signup_details(db.Model):
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    EnterYourEmail= db.Column(db.String(20), nullable=False)
    PhoneNo = db.Column(db.String(20), nullable=False)
    City= db.Column(db.String(20), nullable=False)
    EnterYourPassword=db.Column(db.String(20), nullable=False)
    ConfirmPassword=db.Column(db.String(20), nullable=False)
    Date=db.Column(db.String(20),nullable=True)
    SNo = db.Column(db.Integer, primary_key=True)

@app.route("/", methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        #entry fetched from the db
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        #date = request.form('Date')

        #adding entry to the db
        entry = Signup_details(FirstName=firstname, LastName=lastname, EnterYourEmail=email, PhoneNo=phone,
                               City=city, EnterYourPassword=password, ConfirmPassword=confirm
                               ,Date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        #added entry to db
    return render_template('main.html')

@app.route("/signup")
def register():
    #name="xyz"
    return render_template('about.html') #name2= name

@app.route("/forgetpass_register")
def fogetpass_register():
    return render_template('forgetpass_register.html')

app.run()

'''from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/yatri_signup'
db = SQLAlchemy(app)

'''
'''First Name, Last Name, Enter your email, Phone no., City, Enter your password, Confirm password, date, s.no.'''
'''

class Signup_details(db.Model):
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    EnterYourEmail= db.Column(db.String(20), nullable=False)
    PhoneNo = db.Column(db.String(20), nullable=False)
    City= db.Column(db.String(20), nullable=False)
    EnterYourPassword=db.Column(db.String(20), nullable=False)
    ConfirmPassword=db.Column(db.String(20), nullable=False)
    Date=db.Column(db.String(20))
    SNo = db.Column(db.Integer, primary_key=True)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/forgetpass")
def forget_pass():
    return render_template('forgetpass_register.html')
@app.route("/register")
def register():
    return render_template('forgetpass_register.html')
@app.route("forgetpass_register", methods=["GET","POST"])
def contact():
    if(request.method=="POST"):
        firstName=request.form.get('FirstName')
        lastName=request.form.get('LastName')
        enterYourEmail=request.form.get('EnterYourEmail')
        phoneNo=request.form.get('PhoneNo')
        city=request.form.get('City')
        enterYourPassword=request.form.get('EnterYourPassword')
        confirmPassword=request.form.get('ConfirmPassword')
        date=request.form('Date')
        entry=Signup_details(FirstName=firstName,  LastName=lastName, EnterYourEmail=enterYourEmail, PhoneNo=phoneNo, City=city, EnterYourPassword=enterYourPassword, ConfirmPassword=confirmPassword, Date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('forgetpass_register.html')
app.run(debug=True)
'''