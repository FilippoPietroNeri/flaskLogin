from flask import Flask, render_template, request, redirect, Response
import pandas as pd
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('login.html')

@app.route('/login/fetch', methods=['POST'])
def login2handle():
    if request.method == "POST":
        databaseutenti = pd.read_csv('databaseutenti.csv')
        json = request.get_json()
        username = json.get('username')
        password = json.get('password')
        
        checkUser = databaseutenti[(databaseutenti['Username'] == username) & (databaseutenti['Password'] == password)]
        if len(checkUser) == 0:
            return { "code": 401, "message": "Invalid Username or Password" }, 401
        return { "code": 200, "message": "Logged", "user": checkUser.to_json(orient='records') }, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)