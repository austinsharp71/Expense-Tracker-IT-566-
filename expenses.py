# expenses.py
# Add, print, and filter expenses.
# Each expense is a dictionary with a date, category, description, and amount.


def add_expense(expense_list):
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    expense = {"date": date, "category": category, "description": description, "amount": amount}
    expense_list.append(expense)
    print("Expense added.")


def print_expenses(expense_list):
    if len(expense_list) == 0:
        print("No expenses found.")
    for expense in expense_list:
        print(expense["date"] + " " + expense["category"] + " " + expense["description"] + " " + expense["amount"])


def filter_expenses(expense_list):
    print("Press Enter to skip any filter.")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    category = input("Category: ")
