from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import auth

app = Flask(__name__)

# Initialize Firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("quizweb-app-python-firebase-adminsdk-sruo0-1c03b20ea3.json")
firebase_admin.initialize_app(cred)


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            print('Successfully created user:', user.uid)
            return redirect('/login')
        except Exception as e:
            print('Error creating user:', e)

    return render_template('sign_up.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Add login route and other routes as needed

if __name__ == '__main__':
    app.run(debug=True)
