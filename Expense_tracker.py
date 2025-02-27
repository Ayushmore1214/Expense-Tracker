import csv
import datetime
import os
import matplotlib.pyplot as plt

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to check if the file exists, if not, create it
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    description = input("Enter description: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    print("\n✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if len(expenses) == 1:
                print("\n📂 No expenses recorded yet.\n")
                return

            print("\n📋 Your Expenses:\n")
            for row in expenses:
                print("\t".join(row))
    except FileNotFoundError:
        print("\n⚠️ No expenses found. Add some first!\n")

# Function to generate a report
def generate_report():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            category_totals = {}

            for row in reader:
                category = row[2]
                amount = float(row[1])
                category_totals[category] = category_totals.get(category, 0) + amount

            print("\n📊 Expense Report by Category:\n")
            for category, total in category_totals.items():
                print(f"{category}: ₹{total:.2f}")

            # Visualizing expenses using matplotlib
            if category_totals:
                plt.figure(figsize=(8, 5))
                plt.bar(category_totals.keys(), category_totals.values(), color='skyblue')
                plt.xlabel("Category")
                plt.ylabel("Total Expense")
                plt.title("Expense Distribution by Category")
                plt.xticks(rotation=45)
                plt.show()
    except FileNotFoundError:
        print("\n⚠️ No expenses found. Add some first!\n")

# Main menu function
def main():
    initialize_file()

    while True:
        print("\n💰 Expense Tracker 💰")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Generate Report")
        print("4️⃣ Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("\n👋 Exiting Expense Tracker. Have a great day!\n")
            break
        else:
            print("\n❌ Invalid option! Please choose again.\n")

if __name__ == "__main__":
    main()
