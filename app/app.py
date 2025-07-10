from flask import Flask,request,render_template,redirect
import _mysql_connector as sql

cur=sql.cursor()


app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')