from flask import Flask, send_file

app = Flask(__name__)
app.config.update(
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route('/download')
def downlaod():
    return send_file('dummy_file')

app.run(port = 5000)
