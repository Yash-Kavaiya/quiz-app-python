from flask import Flask, render_template, request, redirect, url_for
# from flask_firebase import Firebase

app = Flask(__name__)

# # Configure Firebase
# firebase = Firebase(app)

# # Database schema
# users = firebase.database().collection('users')
# questions = firebase.database().collection('questions')
# quizzes = firebase.database().collection('quizzes')
@app.route("/")
def index():
    return render_template("index.html")
# # User authentication
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Create a new user in Firebase
#         user = users.add({
#             'username': username,
#             'email': email,
#             'password': password
#         })

#         # Log the user in
#         firebase.auth().sign_in_with_email_and_password(email, password)

#         # Redirect the user to the homepage
#         return redirect(url_for('homepage'))

#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Log the user in
#         firebase.auth().sign_in_with_email_and_password(email, password)

#         # Redirect the user to the homepage
#         return redirect(url_for('homepage'))

#     return render_template('login.html')

# # Quizzes
# @app.route('/quizzes')
# def quizzes():
#     # Get all quizzes from the Firebase database
#     quizzes = quizzes.get().all()

#     return render_template('quizzes.html', quizzes=quizzes)

# @app.route('/quiz/<quiz_id>')
# def quiz(quiz_id):
#     # Get the quiz from the Firebase database
#     quiz = quizzes.document(quiz_id).get()

#     return render_template('quiz.html', quiz=quiz)

# @app.route('/quiz/<quiz_id>/take', methods=['GET', 'POST'])
# def take_quiz(quiz_id):
#     # Get the quiz from the Firebase database
#     quiz = quizzes.document(quiz_id).get()

#     # Get the user's answers
#     answers = request.form.getlist('answer')

#     # Score the quiz
#     score = 0
#     for i in range(len(quiz['questions'])):
#         if answers[i] == quiz['questions'][i]['correct_answer']:
#             score += 1

#     # Store the quiz results in the Firebase database
#     quizzes.document(quiz_id).collection('results').add({
#         'user_id': firebase.auth().current_user.uid,
#         'score': score
#     })

#     return render_template('quiz_results.html', quiz=quiz, score=score)

# # Homepage
# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     if firebase.auth().current_user:
#         # Get all quizzes from the Firebase database
#         quizzes = quizzes.get().all()

#         return render_template('homepage.html', quizzes=quizzes)
#     else:
#         return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
