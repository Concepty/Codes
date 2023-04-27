from flask import Flask, render_template, session, request, g, redirect
from orm_stub import *


app = Flask(__name__)

@app.before_request
def before_request():
    pass

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/login", methods = ['POST'])
def login():
    if not request.args.get('user_name'): return redirect('.index')
    else:            
        session['logged_in'] = True
        session['user_name'] = request.args.get('user_name')
    return redirect('.index')

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('index.html')

@app.route('/get_temp_permission')
def get_temp_permission():
    session['temp_permission']
    return render_template('index.html') 


app.run(port = 5000)