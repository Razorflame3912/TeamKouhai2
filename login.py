from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'THE TING GO SKRRRA PA PA KA KA KA'


@app.route('/', methods=['GET','POST'])
def root():
    if 'logout' in request.form:
        session.pop('user')
        session.pop('pass')
    elif 'user' in session:
        return redirect(url_for('welcome'))

    return render_template('login.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():

    if 'user' not in session:
        if 'username' not in request.form or request.form['username'] == u'':
            return render_template('error.html', err='forgot your username')
        else:
            enteredUser = request.form['username']
            # print repr(enteredUser)

        if 'pass' not in request.form or request.form['pass'] == u'':
            return render_template('error.html', err='forgot your password')
        else:
            enteredPass = request.form['pass']
            # print enteredPass
        if enteredUser == 'Luke' and enteredPass == 'fourwordsalluppercase':
            session['user'] = enteredUser
            session['pass'] = enteredPass
        else:
            return render_template('error.html', err='typed an incorrect username and password')

    return render_template('welcome.html',name=session['user'])

if __name__ == '__main__':
    app.debug = True
    app.run()
