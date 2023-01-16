from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Errors/404.html'), 404

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def hello(name):
    return render_template('user.html', name=name)


if __name__=='__main__':
    app.run(debug=True)