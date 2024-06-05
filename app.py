from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# In-memory user store
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Middleware to check authentication
@app.before_request
def check_authentication():
    if request.endpoint not in ['login', 'static'] and not current_user.is_authenticated:
        return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Example leaderboard data
    leaderboard = [
        {'name': 'User1', 'score': 95},
        {'name': 'User2', 'score': 90},
        {'name': 'User3', 'score': 85},
        {'name': 'User4', 'score': 80},
        {'name': 'User5', 'score': 75},
        {'name': 'User6', 'score': 70},
        {'name': 'User7', 'score': 65},
        {'name': 'User8', 'score': 60},
        {'name': 'User9', 'score': 55},
        {'name': 'User10', 'score': 50}
    ]
    return render_template('dashboard.html', leaderboard=leaderboard)

@app.route('/talati')
@login_required
def talati():
    return render_template('talati.html')

@app.route('/learn')
@login_required
def learn():
    return render_template('learn.html')

if __name__ == '__main__':
    app.run(debug=True)