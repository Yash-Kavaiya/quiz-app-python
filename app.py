from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def results():
    answers = request.args
    return render_template('index.html')
@app.route('/login')
def login():
    if request.method == "POST":
        print(username)
        print(password)
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if user["username"] == username and user["password"] == password:
                # User is logged in
                return redirect("/")
        # User is not logged in
        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")
    
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
  if request.method == "GET":
    return render_template("sign_up.html")

  # Get the email and password from the request
  email = request.form.get("email")
  password = request.form.get("password")

  # Create a new Firebase user account
  user = auth.create_user(email=email, password=password)

  # Send a verification email to the new user
  auth.send_email_verification(user.uid)

  # Redirect the user to the Firebase OTP page
  return redirect("https://firebase.google.com/otp/email/send?uid={}".format(user.uid))
if __name__ == '__main__':
    app.run(debug=True)