from flask import Flask, render_template, session, request, g, redirect, url_for
from orm_stub import *
from access_control.methods import *


app = Flask(__name__)
app.config.update(
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

def render(inner_template, **kwargs):
    return render_template('base.html', inner_template = inner_template, **kwargs)    

@app.before_request
def before_request():
    pass

@app.route('/')
@app.route('/index')
def index():
    return render('index.html')

@app.route("/login", methods = ['POST'])
def login():
    user_name = request.form.get('user_name')
    if not user_name or not find_user_by_name(user_name):
        return redirect(url_for('index'))
    else:
        session['logged_in'] = True
        session['user_name'] = request.args.get('user_name')
    return redirect(url_for('index'))

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/get_temp_permission')
def get_temp_permission():
    session['temp_permission'] = True
    return render('index.html')


@app.route('/journal/<user_name>/<id>')
@check_visitor_permission
def user_journal(user_name: str, id: int):
    id = int(id) - 1
    writer = find_user_by_name(user_name)
    if writer is None: render("journal.html", journal_content = 'No content')
    journal_content = find_user_by_name(user_name).journals[id]
    return render("journal.html", journal_content = journal_content)

app.run(port = 5000)
