#This program trackes exxpenses by allowing user input
#Asuming the user will input the amount, date, category, and description of the expense

#imported the datetime module to validate the date input
from datetime import datetime

#inputs options for category of the expense
ALLOWED_CATEGORIES = (
    "food",
    "groceries",
    "rent",
    "utilities",
    "transport",
    "gas",
    "insurance",
    "subscriptions",
    "entertainment",
    "shopping",
    "health",
    "education"
)


#defined the expense function
class Expense:
    def __init__(self, name, amount, date, category):
        self.name = name
        self.amount = amount
        self.date = date
        self.category = category

#validate the input to ensure amount is a positive number, date is in the correct format, and category is not empty
def get_expense_input():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Must be positive.")
            else:
                break
        except ValueError:
            print("Enter a number.")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format.")

    while True:
        category = input("Enter category: ").strip().lower()
        if category in ALLOWED_CATEGORIES:
            break
        else:
            print(f"Choose from: {', '.join(ALLOWED_CATEGORIES)}")

    while True:
        name = input("Enter description: ")
        if name.strip():
            break
        else:
            print("Cannot be empty.")

    return Expense(name, amount, date, category)


   

# This only runs if you execute expense.py directly
if __name__ == "__main__":
    expense_data = get_expense_input()
    print(f"Expense recorded: {expense_data.name}, ${expense_data.amount}, {expense_data.date}, {expense_data.category}")

