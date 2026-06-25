from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv()

# ---------- Flask App Setup ----------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# ---------- Initialize DB ----------
db = SQLAlchemy(app)

# ---------- Flask-Login Setup ----------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------- Models ----------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)  # Ensure enough length for hashed passwords
    role = db.Column(db.String(50), default='user')  # User/Admin
    
    predictions = db.relationship('Prediction', backref='user', lazy=True)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nitrogen = db.Column(db.Float, nullable=False)
    phosphorus = db.Column(db.Float, nullable=False)
    potassium = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    ph = db.Column(db.Float, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# ---------- Load ML Model ----------
with open('crop_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ---------- Create tables and default admin ----------
with app.app_context():
    db.create_all()

    # Create default admin if not exists
    admin_email = "subramanian638545@gmail.com"
    if not User.query.filter_by(email=admin_email).first():
        hashed_pw = generate_password_hash("admin123", method='pbkdf2:sha256')
        admin = User(username="Admin", email=admin_email, password=hashed_pw, role="admin")
        db.session.add(admin)
        db.session.commit()
        print("✅ Default admin created:", admin_email, "/ admin123")

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
@login_required
def dashboard():
    predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.date.desc()).all()
    return render_template('dashboard.html', predictions=predictions)

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied! Admins only.', 'danger')
        return redirect(url_for('home'))

    users = User.query.all()
    predictions = Prediction.query.order_by(Prediction.date.desc()).all()
    return render_template('admin_dashboard.html', users=users, predictions=predictions)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists! Please log in.', 'warning')
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    try:
        # Get input values from form
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph_value = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Predict crop
        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]])
        predicted_crop = model.predict(features)[0]

        # Save prediction to database
        new_prediction = Prediction(
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            temperature=temperature,
            humidity=humidity,
            ph=ph_value,
            rainfall=rainfall,
            result=predicted_crop,
            user_id=current_user.id
        )
        db.session.add(new_prediction)
        db.session.commit()

        flash(f'Predicted Crop: {predicted_crop}', 'success')
        return redirect(url_for('dashboard'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('home'))

# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)
