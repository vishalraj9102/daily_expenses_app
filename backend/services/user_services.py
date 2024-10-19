from models import db, User
from schemas import UserSchema
from flask import jsonify

user_schema = UserSchema()

def create_user(data):
    errors = user_schema.validate(data)
    if errors:
        return {'error': errors}, 400

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    
    return {'message': 'User created successfully', 'id': new_user.id}, 201

def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return {
        'name': user.name,
        'email': user.email,
        'mobile': user.mobile
    }, 200
