# 💸 Spendly — Expense Tracker

A Python expense tracker that started as a command-line app and grew into a full-stack project: a Flask REST API backed by JSON file storage, with a live browser frontend that talks to it in real time.

## Features

- Add, view, and delete expenses with description, amount, date, and category
- Two ways to use it: a terminal menu, or a browser dashboard
- REST API (Flask) exposing the same functionality over HTTP
- Data persists to `data.json` — survives restarts and browser refreshes
- Input validation on both the CLI and the API (positive amounts, valid dates, allowed categories)
- 12 supported spending categories
- Category breakdown and spending stats in the web dashboard

## Project Structure

```
expense-tracker/
├── main.py             # CLI entry point and menu loop
├── expense.py           # Expense class, allowed categories, CLI input validation
├── storage.py            # JSON read/write management (shared by CLI and API)
├── app.py                # Flask REST API (GET/POST/DELETE /api/expenses)
├── app_frontend.html      # Browser dashboard — talks to app.py live via fetch()
├── data.json              # Saved expense data (created automatically, gitignored for testers)
└── requirements.txt        # Python dependencies
```

## Requirements

- Python 3.x
- Flask
- Flask-CORS

Install dependencies with:

```bash
pip install -r requirements.txt
```

(If `pip` isn't recognized on Windows, try `py -m pip install -r requirements.txt`.)

## How to Run

### Option A — Command line

```bash
python main.py
```

```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
```

### Option B — Web dashboard

1. Start the API server:
   ```bash
   python app.py
   ```
   This runs at `http://127.0.0.1:5000`.

2. Open `app_frontend.html` in a browser (a "Live Server" style extension works well, but isn't required).

3. Add and delete expenses through the dashboard — changes are saved to `data.json` via the API and persist across refreshes.

> Both the CLI and the web dashboard read/write the same `data.json` file through `storage.py`, so either interface will reflect changes made through the other.

## API Reference

| Method | Route            | Description                          |
|--------|------------------|---------------------------------------|
| GET    | `/api/expenses`  | Returns all saved expenses as JSON    |
| POST   | `/api/expenses`  | Adds a new expense (JSON body: `name`, `amount`, `date`, `category`) |
| DELETE | `/api/expenses`  | Deletes an expense matching `name` and `date` (sent as a JSON body) |

Validation returns `400` with an error message for malformed input; a delete request with no matching expense returns `404`.

## Supported Categories

| Category | Category | Category |
|---|---|---|
| food | groceries | rent |
| utilities | transport | gas |
| insurance | subscriptions | entertainment |
| shopping | health | education |

## Design Notes

- **Why delete matches on name + date, not a unique ID:** the current implementation identifies an expense by its name and date together, which is a reasonable approach for a single-user tool but isn't collision-proof (two same-day, same-name expenses would be ambiguous). A future refactor would give each expense a generated unique ID at creation time instead.
- **CORS:** the frontend and API run on different local ports during development, so `flask-cors` is used to explicitly allow the browser to read API responses.

## What I Learned

- Structuring a multi-file Python project
- Object-oriented programming with classes
- Reading and writing JSON data for persistence
- Input validation with loops and exception handling
- Building a REST API with Flask — routes, HTTP methods, status codes, request/response bodies
- The difference between server-side data (JSON file) and client-side state (JS variables), and why persistence requires the former
- Debugging CORS issues between a frontend and backend running on different ports
- Reasoning through data-integrity tradeoffs (identifying records by index vs. name/date vs. unique ID)

