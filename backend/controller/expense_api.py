from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.expense_services import add_expense, get_expenses, download_balance_sheet
from Dto.expense_dto import expense_responses, get_expenses_responses, download_balance_sheet_responses

expense_api = Blueprint('expense_api', __name__)



# Add Expense
@expense_api.route('/expense', methods=['POST'])
@swag_from(expense_responses)
def add_expense_route():
    data = request.get_json()
    try:
        return add_expense(data)
    except Exception as e:
        # Log the exception or return a more specific error message
        return jsonify({'error': str(e)}), 400



# Retrieve User Expenses
@expense_api.route('/expenses/<int:user_id>', methods=['GET'])
@swag_from(get_expenses_responses)
def get_expenses_route(user_id):
    try:
        return get_expenses(user_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 404



# Download Balance Sheet
@expense_api.route('/balance_sheet/<int:user_id>', methods=['GET'])
@swag_from(download_balance_sheet_responses)
def download_balance_sheet_route(user_id):
    try:
        return download_balance_sheet(user_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 404
