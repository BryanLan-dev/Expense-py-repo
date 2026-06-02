from storage import StorageManager
from expense import Expense, get_expense_input


def main():
# Initialize the storage manager
    manager = StorageManager()

# Main loop for the application
    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Exit')
        
# Get user choice
        choice = input('Enter your choice: ')
        if choice == '1':
            exp = get_expense_input()
            manager.add_expense(exp)
            print('Expense added successfully!')
        elif choice == '2':
            expenses = manager.load_expenses()
            if not expenses:
                print('No expenses found.')
            else:
                for exp in expenses:
                    print(f'{exp.date}: {exp.name} - ${exp.amount:.2f}')

        elif choice == '3':
            print('Exiting the application. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the main function
if __name__ == '__main__':
    main()