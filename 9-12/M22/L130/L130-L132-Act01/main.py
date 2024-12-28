from flask import Flask, render_template, request
import mysql
import re

app = Flask(__name__)

@app.route("/login" , methods=['POST' , 'GET'])

def login():
    msg = ""

    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]

        mydb = mysql.connector.connect(
            host = "remotemysql.com",
            user = "Rz8hqn1dK4",
            password = "nd0WKO3xeO",
            database = "Rz8hqn1dK4"
        )

        mycursor = mydb.cursor()
        mycursor.execute("select * from LoginDetails where Name = %s AND Password = %s", (username, password))
        account = mycursor.fetchone()

        if account:
            print("login success")
            name = account[1]
            id = account[0]
            msg = "logged in successfully"
            print("login successfull")
            return render_template("welcome.html", msg-msg, name=name, id=id)
        else:
            msg = "username not found. please try again"
            return render_template("login.html", msg=msg)
    
    else:
        return render_template("login.html")
    
@app.route("/logout" , methods=['POST' , 'GET'])
def logout():
    name = ""
    id = ""
    msg = "Logout successfully"

    return render_template("login.html", msg-msg, name=name, id=id)

@app.route("/register" , methods=['POST' , 'GET'])
def register():
    if request.method == "POST" and "username" in request.form and "password" in request.form and "email" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        mydb = mysql.connector.connect(
            host = "remotemysql.com",
            user = "Rz8hqn1dK4",
            password = "nd0WKO3xeO",
            database = "Rz8hqn1dK4"
        )

        mycursor = mydb.cursor()
        print(username)
        mycursor.execute("select * from LoginDetails where Name = %s AND Email_id = %s", (username, email))
        account = mycursor.fetchone()
        print(account)

        if account :
            msg = "Account already exist"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email) :
            msg = "invalid email address"
        elif not re.match(r"[A-Za-z0-9]+", username) :
            msg = "username can only contain letters and numbers"
        elif not username or not password or not email:
            msg = "kindly fill the details"
        else:
            mycursor.execute("insert into LoginDetails values(NULL, %s, %s, %s)", (username, password, email))
            mydb.commit()
            msg = "registration success"
            name = username
            return render_template("welcome.html", msg=msg, name=name)
    elif request.method == "POST":
        msg = "kindly fill the details"
    
    return render_template("registration.html", msg=msg)