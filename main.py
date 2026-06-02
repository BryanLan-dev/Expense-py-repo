from storage import StorageManager
from expense import expense


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
            description = input('Enter expense description: ')
            amount = float(input('Enter expense amount: '))
            date = input('Enter expense date (YYYY-MM-DD): ')
            exp = expense(description, amount, date)
            manager.add_expense(exp)
            print('Expense added successfully!')
        elif choice == '2':
            expenses = manager.get_expenses()
            if not expenses:
                print('No expenses found.')
            else:
                for exp in expenses:
                    print(f'{exp.date}: {exp.description} - ${exp.amount:.2f}')
        elif choice == '3':
            print('Exiting the application. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the main function
if __name__ == '__main__':
    main()