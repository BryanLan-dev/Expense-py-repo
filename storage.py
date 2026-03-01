
import json
import os

class StorageManager:
    
    def __init__(self, filename="data.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f) 
    
    def load_expenses(self):
        with open(self.filename, "r") as f:
            data = json.load(f)
            


    def save_expenses(self, expenses):
        with open(self.filename, "w") as f:
            json.dump(expenses, f)

    
    def add_expense(self, expense):
        expenses = self.load_expenses()
        expenses.append(expense)
        self.save_expenses(expenses)
