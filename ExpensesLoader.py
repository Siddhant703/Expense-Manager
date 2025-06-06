from Expense import *


class ExpensesLoader(object):
    """A class for loading expenses from a file.
    """

    # We do not have an __init__ function and will call the default constructor

    def import_expenses(self, expenses, file):
        """Reads data from the given file and stores the expenses in the given expenses dictionary, where the expense
        type is the key and the value is an Expense object with the parameters expense type and total amount for that
        expense type.

        The same expense type may appear multiple times in the given file, so add all the amounts for the same
        expense types.

        Ignore expenses with missing amounts. If a line contains both an expense type and an expense amount,
        they will be separated by a colon (:).

        You can assume that if they exist, expense types are one-word strings and the amounts are numerical and can
        be casted to a float data type.

        Strip any whitespace before or after the expense types and amounts. Blank lines should be ignored.

        Expenses are case-sensitive. "coffee" is different from "Coffee".

        This method will be called twice in the main function in expenses.py with the same dictionary, but different
        files.

        This method doesn’t return anything.  Rather, it updates the given expenses dictionary based
        on the expenses in the given file.

        For example, after loading the expenses from the file, the expenses dictionary should look like
        this: {'food': Expense('food', 5.00), 'coffee': Expense('coffee', 12.40),
               'rent': Expense('rent', 825.00), 'clothes': Expense('clothes', 45.00),
               'entertainment': Expense('entertainment', 135.62), 'music': Expense('music', 324.00),
               'family': Expense('family', 32.45)}

        Note: You are not expected to handle negative numbers in your code
        """
        # read data from given file and extract all sentences as a list
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        lines = [x for x in lines if x] #ignoring blank lines in txt file

        # iterating over each sentence in the file to extract relevant info
        for line in lines:
            expense_type = str(line.split(':')[0].strip()) #extracting expense type
            # error handling to ensure amount can be converted to float
            try:
                amount = float(line.split(':')[1]) #extracting amount
            except:
                continue
            # if statement to handle the case where expense type is already in the dictionary
            if expense_type in expenses:
                new_amount = expenses[expense_type].amount + amount #add new amount to existing amount for existing expense type
                expenses[expense_type] = Expense(expense_type, new_amount) #appending new amount to existing expense object
                continue
            else:
                expenses.update({expense_type: Expense(expense_type, amount)}) #creating a new expense object
        # TODO insert your code