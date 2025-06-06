# Expense Management System

This is a command-line Python program for managing expenses. Users can load expenses from files, modify them, sort and export filtered expenses, and run tests to validate the system. This project was implemented as part of a structured programming exam.

## Project Structure

.
├── expenses.py # Main entry point (DO NOT MODIFY)
├── ExpensesLoader.py # Loads expense data from files
├── ExpensesManager.py # Core logic for managing and processing expenses
├── Expense.py # Defines the Expense class
├── expenses_test.py # Unit tests for the system
├── expenses.txt # Input file 1 (DO NOT MODIFY)
├── expenses_2.txt # Input file 2 (DO NOT MODIFY)
└── README.md # Project documentation

pgsql
Copy
Edit

## Features

- Load expenses from two `.txt` files into a single dictionary
- Combine duplicate expense types by summing their values
- Add to, deduct from, or update existing expenses
- Sort expenses by type (ascending) or amount (descending)
- Export selected expense types to a new file
- Ignores malformed or blank lines during import
- Handles missing data gracefully
- Case-sensitive handling of expense types
- Includes unit tests with the ability to add more

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/expense-management-system.git
cd expense-management-system
Run the main program:

bash
Copy
Edit
python expenses.py
Run the tests:

bash
Copy
Edit
python -m unittest expenses_test.py
Input File Format (expenses.txt, expenses_2.txt)
Each line in the input files should be formatted as:

makefile
Copy
Edit
expense_type: amount
Example:

yaml
Copy
Edit
coffee: 3.50
rent: 1000.00
entertainment: 55.25
Lines without a colon or a numeric amount are ignored

Blank lines are skipped

Whitespace is stripped from both sides

Expense types are case-sensitive (Coffee and coffee are different)

Duplicate types in the same file are combined

Testing
Run expenses_test.py using Python's unittest framework:

bash
Copy
Edit
python -m unittest expenses_test.py
You are encouraged to add distinct test cases to ensure full coverage. Provided tests check:

Expense importing

Adding, deducting, and updating expenses

Sorting behavior

Exporting filtered expenses

Proper exception handling and messages

Implementation Notes
Do not modify expenses.py; this is the main program entrypoint used by the autograder

Implement all specified methods in:

ExpensesLoader.py

ExpensesManager.py

Expense.py

All methods must match their given names and signatures exactly

Remove all raise NotImplementedError lines after implementing the methods

Add meaningful comments and docstrings for all helper methods you create

Example Behavior
Add to an existing expense:

Input: coffee, 1.32

Output: coffee: 13.72

Deduct from an expense:

If value exceeds the current amount, raise RuntimeError

Export to file:

Only exports matching expense types; overwrites the file if it exists

Submission Checklist
Your repository should include:

expenses.py (unchanged)

ExpensesLoader.py, ExpensesManager.py, and Expense.py (fully implemented)

expenses_test.py (with your additional tests)

expenses.txt and expenses_2.txt (unchanged)

vbnet
Copy
Edit
