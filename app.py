from flask import Flask, jsonify, render_template, request, Response, make_response
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

def get_list():
    return ["This page", "is rendered", "with Flask"]

@app.route('/about')
def about():
    return render_template('about.html', about=get_list())

@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)

@app.route('/time')
def time():
    ret_data = {"value": random.randint(0,1000)}
    return jsonify(ret_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
