from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def principal():
    return 'esta es la pajina principal' 

@app.route('/inicio')
def inicio():
    return 'este es el inicio' 