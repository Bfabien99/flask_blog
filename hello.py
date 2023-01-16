from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from flask import Flask, render_template

from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm

from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap5(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'bvuyhgvbkjhkj++'

class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('Errors/404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    names = None
    form = NameForm()
    if form.validate_on_submit():
        print(form.name.data)
        names = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=names)

@app.route('/user/<name>')
def hello(name):
    return render_template('user.html', name=name)


if __name__=='__main__':
    app.run(debug=True)