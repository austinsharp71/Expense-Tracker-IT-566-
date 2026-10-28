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
