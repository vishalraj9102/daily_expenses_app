from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.user_services import create_user, get_user
from Dto.users_dto import user_creation_responses, user_retrieval_responses

user_api = Blueprint('user_api', __name__)

# Create User
@user_api.route('/user', methods=['POST'])
@swag_from(user_creation_responses)
def create_user_route():
    data = request.get_json()
    return create_user(data)

# Retrieve User
@user_api.route('/user/<int:user_id>', methods=['GET'])
@swag_from(user_retrieval_responses)
def get_user_route(user_id):
    return get_user(user_id)
