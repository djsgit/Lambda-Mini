from flask import Flask, render_template, jsonify

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify it's behavior

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'February 21 1985'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello, %s' % name

@app.route('/sum/<int1>/<int2>')
def sum(int1, int2):
    total = int(int1) + int(int2)
    return str(total)

@app.route('/multiply/<int1>/<int2>')
def prod(int1, int2):
    total = int(int1) * int(int2)
    return str(total)

@app.route('/subtract/<int1>/<int2>')
def diff(int1, int2):
    total = int(int1) - int(int2)
    return str(total)

@app.route('/favoritefoods')
def myList():
    myList = ['Sashimi', 'Pizza', 'Watermelon']
    return jsonify(myList)
    
