from flask import Flask, render_template, request, redirect
import pandas as pd
app = Flask(__name__)

@app.route('/')
def homepage():
    print(request.args.get('error'))
    if request.args.get('error'):
        print("ok")
        return render_template('index.html', error=request.args.get('error'))
    return render_template('index.html')

@app.route('/test')
def homepaget():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def loginhandle():
    if request.method == "POST":
        databaseutenti = pd.read_csv('databaseutenti.csv')
        username = request.form.get('username')
        password = request.form.get('password')
        
        checkUser = databaseutenti[(databaseutenti['Username'] == username) & (databaseutenti['Password'] == password)]
        if len(checkUser) == 0:
            return redirect('/?error=Invalid username or password.', code=302)
        return render_template('result.html', username=username)

@app.route('/login/fetch', methods=['POST'])
def login2handle():
    if request.method == "POST":
        databaseutenti = pd.read_csv('databaseutenti.csv')
        json = request.get_json()
        username = json.get('username')
        password = json.get('password')
        
        checkUser = databaseutenti[(databaseutenti['Username'] == username) & (databaseutenti['Password'] == password)]
        if len(checkUser) == 0:
            return redirect('/test?error=Invalid username or password.', code=302)
        return render_template('result.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)