import csv
import os
from datetime import datetime
import pandas as pd
DATA_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Travel', 'Bills', 'Shopping', 'Other']
def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])
def add_expense():
    try:
        amount = float(input("Enter amount (Rs): "))
        category = input(f"Enter category {CATEGORIES}: ")
        if category not in CATEGORIES:
            print("Invalid category!")
            return
        description = input("Enter description: ")
        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        date = datetime.today().date() if not date_str else datetime.strptime(date_str, "%Y-%m-%d").date()
        with open(DATA_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, amount, category, description])
        print("Expense added.")
    except ValueError:
        print("Invalid input. Try again.")
def view_expenses():
    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
    print("\n--- All Expenses ---")
    print(df.to_string(index=False))
def show_summary():
    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby(['Month', 'Category'])['Amount'].sum().reset_index()
    print("\n--- Monthly Summary ---")
    print(summary.to_string(index=False))
def export_csv():
    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    summary = df.groupby(['Month', 'Category'])['Amount'].sum().reset_index()
    summary.to_csv('monthly_summary.csv', index=False)
    print("Summary exported to 'monthly_summary.csv'")
def main():
    init_file()
    while True:
        print("\n=== Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Monthly Summary")
        print("4. Export Summary to CSV")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            export_csv()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
