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
    print('==========================')
    print("session['logged_in']", session.get('logged_in'))
    print("session['user_name']", session.get('user_name'))
    print("session['temp_permission']", session.get('temp_permission'))
    print('args', dict.items(request.args))
    print('forms', dict.items(request.form))

    

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
        session['user_name'] = request.form.get('user_name')
    return redirect(url_for('index'))

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/get_temp_permission')
def get_temp_permission():
    session['temp_permission'] = True
    return render('index.html')


@app.route('/journal')
@check_visitor_permission
def user_journal():
    id = int(request.args.get('id', 1)) - 1
    writer = find_user_by_name(request.args.get('journal_user'))
    if writer is None: render("journal.html", journal_content = 'No content')
    journal_content = find_user_by_name(request.args.get('journal_user')).journals[id]
    return render("journal.html", journal_content = journal_content)

app.run(port = 5000)
