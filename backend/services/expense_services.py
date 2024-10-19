from jsonschema import ValidationError
from models import db, Expense, User
from schemas import ExpenseSchema
from flask import jsonify
import json

expense_schema = ExpenseSchema()

def add_expense(data):
    # Initialize the schema with the context
    expense_schema = ExpenseSchema(context={'amount': data.get('amount')})

    # Validate input data using the schema
    try:
        expense_schema.load(data)  # Validate the data
    except ValidationError as errors:
        return {'error': errors.messages}, 400

    # Prepare data for the Expense object
    exact_splits = json.dumps(data.get('exact_splits', {})) if data.get('exact_splits') else '{}'
    percentage_splits = json.dumps(data.get('percentage_splits', {})) if data.get('percentage_splits') else '{}'
    participants = data.get('participants', [])  # Get participants from input
    description = data.get('description')  # Get description from input

    # Create a new Expense object
    new_expense = Expense(
        amount=data['amount'],
        split_method=data['split_method'],
        description=description,  # Use description from input
        user_id=data['user_id'],
        exact_splits=exact_splits,  # Store as JSON string
        percentage_splits=percentage_splits,  # Store as JSON string
        participants=participants  # Store participants directly
    )
    
    # Add to the session and commit
    db.session.add(new_expense)
    db.session.commit()

    return {'message': 'User created successfully', 'id': new_expense.id}, 201



def get_expenses(user_id):
    user = User.query.get_or_404(user_id)
    expenses = [{'amount': e.amount, 'method': e.split_method} for e in user.expenses]
    return jsonify(expenses), 200

def download_balance_sheet(user_id):
    user = User.query.get_or_404(user_id)
    expenses = [{'amount': e.amount, 'method': e.split_method} for e in user.expenses]
    
    # Convert to CSV format
    balance_sheet = f"Balance Sheet for {user.name}\n" + "\n".join([f"{e['amount']} ({e['method']})" for e in expenses])
    
    # Return as a plain text response
    return balance_sheet, 200, {'Content-Type': 'text/plain'}
