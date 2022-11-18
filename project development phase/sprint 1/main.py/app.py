from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

app = Flask(_name_)
@app.route('/')
def home():
    return render_template('login page.html')
@app.route('/register')
def register():
    return render_template('registration.html')

if _name_ == '_main_':
   app.run(debug=True)