# main.py
# Expense Tracker - run this file to start the program.

import expenses
import file_handler

expense_list = []

while True:
    print()
    print("--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Filter expenses")
    print("4. Save to JSON file")
    print("5. Open JSON file")
    print("6. Export to CSV")
    print("7. Quit")
    choice = input("Choose 1-7: ")

    if choice == "1":
        expenses.add_expense(expense_list)
    elif choice == "2":
        expenses.print_expenses(expense_list)
    elif choice == "3":
        expenses.filter_expenses(expense_list)
    elif choice == "4":
        file_handler.save_json(expense_list)
    elif choice == "5":
        expense_list = file_handler.open_json()
    elif choice == "6":
        file_handler.export_csv(expense_list)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Pick 1-7.")
