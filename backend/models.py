from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON

# Initialize the SQLAlchemy instance here
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)

    expenses = db.relationship('Expense', backref='users', lazy=True)


class Expense(db.Model):
    __tablename__ = 'expenses'  # Make sure to set the table name if you haven't
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    split_method = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Additional fields for split amounts
    exact_splits = db.Column(db.String(500))  # Store exact splits as JSON
    percentage_splits = db.Column(db.String(500))  # Store percentage splits as JSON

    # Add this line to include participants
    participants = db.Column(JSON)  
