#This program trackes exxpenses by allowing user input
#Asuming the user will input the amount, date, category, and description of the expense

#imported the datetime module to validate the date input
from datetime import datetime

#inputs options for category of the expense
ALLOWED_CATEGORIES = ALLOWED_CATEGORIES = (
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
def expense():

#validate the input to ensure amount is a positive number, date is in the correct format, and category is not empty
    while True:
            try:
                amount = float(input("Enter the amount of the expense: "))
                if amount <= 0:
                    print("Amount must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
    
    while True:
            date = input("Enter the date of the expense (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
    
    while True:
        category = input("Enter the category of the expense (e.g., food, rent, transport): ").strip().lower()
        if category in ALLOWED_CATEGORIES:
            break
        else:
            print(f"Invalid category. Please choose from: {', '.join(ALLOWED_CATEGORIES)}")

    while True:
        description = input("Enter a description for the expense: ")
        if description.strip() == "":
            print("Description cannot be empty or contain only spaces. Please try again.")
        else:
            break


    expense_data = {
    "amount": amount,
    "date": date,
    "category": category,
    "description": description,
}

    return expense_data

# This only runs if you execute expense.py directly
if __name__ == "__main__":
    expense_data = expense()
    print("Expense recorded:", expense_data)

