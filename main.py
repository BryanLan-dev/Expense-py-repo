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
        print('3. Delete Expense')
        print('4. Exit')

# Get user choice
        choice = input('Enter your choice: ')
        
        # Handle user choices
        if choice == '1':
            exp = get_expense_input()
            manager.add_expense(exp)
            print('Expense added successfully!')
        
        # Handle viewing expenses
        elif choice == '2':
            expenses = manager.load_expenses()
            if not expenses:
                print('No expenses found.')
            else:
                for exp in expenses:
                    print(f'{exp.date}: {exp.name} - ${exp.amount:.2f}')
        
        # Handle deleting expenses
        elif choice == '3':
            expenses = manager.load_expenses()
            if not expenses:
                print('No expenses to delete.')
            else:
                for idx, exp in enumerate(expenses):
                    print(f'{idx + 1}. {exp.date}: {exp.name} - ${exp.amount:.2f}')
                try:
                    del_idx = int(input('Enter the number of the expense to delete: ')) - 1
                    if 0 <= del_idx < len(expenses):
                        manager.delete_expense(del_idx)
                        print('Expense deleted successfully!')
                    else:
                        print('Invalid index. Please try again.')
                except ValueError:
                    print('Invalid input. Please enter a number.')

        # Handle exiting the application
        elif choice == '4':
            print('Exiting the application. Goodbye!')
            break
        
        # Handle invalid choices
        else:
            print('Invalid choice. Please try again.')

# Run the main function
if __name__ == '__main__':
    main()