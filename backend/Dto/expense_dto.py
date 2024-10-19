expense_responses = {
    201: {'description': 'Expense added successfully'},
    400: {'description': 'Invalid data'},
}

get_expenses_responses = {
    200: {'description': 'User expenses retrieved'},
    404: {'description': 'User not found'},
}

download_balance_sheet_responses = {
    200: {'description': 'Balance sheet generated'},
    404: {'description': 'User not found'},
}
