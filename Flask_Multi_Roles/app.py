from flask import Flask, redirect, request, render_template, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from flask_login import LoginManager, logout_user, login_user, login_required
from flask_migrate import Migrate
from functools import wraps


login_manager = LoginManager()

app = Flask(__name__)

#SQLAlchemy Settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisismihan'

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = "index"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def login_required_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You are not Admin")
            return redirect(url_for('index'))

    return wrap

    
def login_required_user(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in_user' in session:
            return f(*args, **kwargs)
        else:
            flash("You are not Admin")
            return redirect(url_for('index'))

    return wrap

#MODALS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(254))
    role = db.Column(db.String(100))



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name=name).first()
        login_user(user) 
        session['role'] = user.role
        if session['role'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('welcome'))
        else:
            session['logged_in_user'] = True
            return redirect(url_for('user'))
    return render_template('index.html')

@app.route('/welcome')
@login_required_admin
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        logout_user()
        session.pop('logged_in', None)
    else:
        logout_user()

    return redirect(url_for('index'))
    
@app.route('/user')
@login_required_user
def user():
    return "You are a user"
if __name__ == '__main__':
    app.run(debug=True)