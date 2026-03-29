from expense import expense
import json
import os


# This function converts an expense object to a dictionary for JSON serialization
def expense_to_dict(expense):
    return {
        "name": expense.name,
        "amount": expense.amount,
        "category": expense.category
    }

# This function converts a dictionary back to an expense object
def dict_to_expense(data):
    return expense(
        data["name"],
        data["amount"],
        data["category"]
    )

# This class manages the storage of expenses in a JSON file
class StorageManager:
    
    # The constructor initializes the storage manager with a filename and creates the file if it doesn't exist
    def __init__(self, filename="data.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f) 
    
    # This method loads expenses from the JSON file and returns them as a list of expense objects
    def load_expenses(self):
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [dict_to_expense(item) for item in data]
            

# This method saves a list of expense objects to the JSON file by converting them to dictionaries
    def save_expenses(self, expenses):
        with open(self.filename, "w") as f:
            json.dump([expense_to_dict(expense) for expense in expenses], f, indent=4)

# This method adds a new expense to the list of expenses and saves it to the JSON file    
    def add_expense(self, expense):
        expenses = self.load_expenses()
        expenses.append(expense)
        self.save_expenses(expenses)
        
