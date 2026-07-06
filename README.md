# 💸 Spendly — Expense Tracker

A command-line expense tracker built in Python that saves your expenses to a local JSON file so your data persists between sessions.

## Features

- Add expenses with description, amount, date, and category
- View all saved expenses sorted by date
- Data saved automatically to `data.json`
- Input validation for amount, date format, and category
- 12 supported spending categories

## Project Structure

```
expense-tracker/
├── main.py        # Entry point and menu loop
├── expense.py     # Expense class and user input logic
├── storage.py     # JSON read/write management
├── data.json      # Saved expense data
└── app_frontend.html  # Visual frontend (open in browser)
```

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python main.py
```

## Usage

```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Exit
```

When adding an expense you will be prompted for:
- **Amount** — must be a positive number
- **Date** — must be in YYYY-MM-DD format
- **Category** — must be one of the 12 allowed categories
- **Description** — cannot be empty

## Supported Categories

| Category | Category | Category |
|---|---|---|
| food | groceries | rent |
| utilities | transport | gas |
| insurance | subscriptions | entertainment |
| shopping | health | education |

## Frontend

Open `app_frontend.html` in any browser for a visual interface to view and manage your expenses.

## What I Learned

- Structuring a multi-file Python project
- Object-oriented programming with classes
- Reading and writing JSON data for persistence
- Input validation with loops and exception handling
- Building a simple CLI menu application
