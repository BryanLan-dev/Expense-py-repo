from flask_cors import CORS
from flask import Flask
from flask import request
import expense
from storage import StorageManager, expense_to_dict
from expense import Expense, get_expense_input

# Initialize the storage manager
manager = StorageManager()

# Flask application instance
app = Flask(__name__) 
CORS(app)

# Define a route for the home page
@app.route('/')
def index():
    return 'Hello World!'

# API endpoint to add a new expense
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = manager.load_expenses()
    return {'expenses': [expense_to_dict(expense) for expense in expenses]}

@app.route('/api/expenses', methods=['POST'])
def post_expenses():
    data = request.get_json()

# Validate the incoming data
    if not all(key in data for key in ['name', 'amount', 'date', 'category']):
        return {'message': 'Invalid expense data!'}, 400
    
    if not isinstance(data['name'], str) or not isinstance(data['category'], str):
        return {'message': 'Name and category must be strings!'}, 400
    elif not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return {'message': 'Amount must be a non-negative number!'}, 400

    # only now, once data looks OK, build the Expense
    new_expense = Expense(data['name'], data['amount'], data['date'], data['category'])
    manager.add_expense(new_expense)
    return {'message': 'Expense added successfully!'}, 201

@app.route('/api/expenses', methods=['DELETE'])
def delete_expense():
    read_data = request.get_json()

    #validate the data coming in
    if not all(key in read_data for key in ['name', 'date']):
        return {'message': 'Invalid deletion data!'}, 400
    # Extract the name and date
    name = read_data['name']
    date = read_data['date']

    # Delete the expense and store the result
    deleted = manager.delete_expense(name, date)

    # Return the appropriate response
    if deleted:
        return {'message': 'Expense deleted successfully!'}, 200
    else:
        return {'message': 'Expense not found!'}, 404


#Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)