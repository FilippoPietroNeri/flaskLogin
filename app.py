from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def loginhandle():
    if request.method == "POST":
        data = request.json
        print(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)