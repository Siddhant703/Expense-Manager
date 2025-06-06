# Expense Management System

This is a command-line Python program for managing expenses. Users can load expenses from files, modify them, sort and export filtered expenses, and run tests to validate the system. This project was implemented as part of a structured programming exam.

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

git clone https://github.com/your-username/expense-management-system.git
cd expense-management-system

2. **Run the main program:**

python expenses.py

3. **Run the tests:**

python -m unittest expenses_test.py

## Input File Format (`expenses.txt`, `expenses_2.txt`)

Each line in the input files should be formatted as:

expense_type: amount

Example:

coffee: 3.50
rent: 1000.00
entertainment: 55.25

- Lines without a colon or a numeric amount are ignored
- Blank lines are skipped
- Whitespace is stripped from both sides
- Expense types are case-sensitive (`Coffee` and `coffee` are different)
- Duplicate types in the same file are combined

## Testing

Run `expenses_test.py` using Python's unittest framework:

python -m unittest expenses_test.py

Tests include:

- Expense importing
- Adding, deducting, and updating expenses
- Sorting behavior
- Exporting filtered expenses
- Exception handling

## Implementation Notes

- Do **not** modify `expenses.py`; it is the program's entry point
- Implement required logic in:
  - `ExpensesLoader.py`
  - `ExpensesManager.py`
  - `Expense.py`
- Keep method names and signatures as specified
- Remove all `raise NotImplementedError` once implemented
- Add meaningful docstrings and comments for helper methods

## Example Behavior

**Add to an existing expense:**

Input: coffee, 1.32
Output: coffee: 13.72

**Deduct from an expense:**

- If the value to deduct exceeds the current amount, raise `RuntimeError`

**Export to file:**

- Only selected expense types are exported
- File is overwritten if it already exists
