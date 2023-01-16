from flask import Flask, request, make_response
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

@app.route('/cookie')
def cookie():
    cook = request.cookies.get('answer', None)
    response = make_response(f'<h1>this page carrie a cookie! {cook}</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__=='__main__':
    app.run(debug=True)