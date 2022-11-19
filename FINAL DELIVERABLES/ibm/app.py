
from flask import Flask,render_template,request,redirect
import db
import os
from db import ibm_db
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/index')
def homepage():
  return render_template("index.html")

@app.route('/home')
def dashboard():
    return render_template("home.html")
@app.route('/contact',methods = ['GET', 'POST'])
def contact():
  return render_template("contact.html")
@app.route('/logout',methods = ['GET', 'POST'])
def logout():
  return render_template("logout.html")
@app.route('/company',methods = ['GET', 'POST'])
def company():
  return render_template("company.html")
@app.route('/job',methods = ['GET', 'POST'])
def job():
  return render_template("job.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    global userid
    msg = ''
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    

    
        
        sql = "SELECT * FROM USERDETAILS WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return render_template("home.html",msg=msg)
               

        else:
            msg = 'Invalid details. Please check the Email ID - Password combination.!'
            return render_template("index.html",msg=msg)
            





@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        sql = "SELECT * FROM USERDETAILS WHERE email = ?"
        stmt = ibm_db.prepare(db.conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg='Job Recommender Account Already exist.kindly login!'
            return render_template("index.html",msg=msg)
       
        else:
            sql ="INSERT INTO USERDETAILS(USERNAME,EMAIL,PHONE,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
            res = ibm_db.exec_immediate(db.conn,sql.format(username,email,phone,password))
            msg = "Your Job Recommender account successfully registered!"
            return render_template("index.html",msg=msg)
        
        


if(__name__=='__main__'):
    
     app.run(host='0.0.0.0',debug=True)


