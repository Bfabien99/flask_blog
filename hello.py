from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def hello(name):
    return render_template('user.html', name=name)


if __name__=='__main__':
    app.run(debug=True)