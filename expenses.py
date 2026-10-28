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
