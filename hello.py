from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>' %name

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s!</h1>' %user_agent

if __name__=='__main__':
    app.run(debug=True)