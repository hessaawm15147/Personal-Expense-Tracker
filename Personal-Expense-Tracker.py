import json  # Import the JSON module to handle saving and loading data
from datetime import datetime  # Import the datetime module to handle dates and times

# Step 1: Load or initialize data
# Try to load existing expenses from 'expenses.json'
# If the file does not exist, initialize an empty list for expenses
try:
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)  # Load expenses from the JSON file
except FileNotFoundError:
    expenses = []  # If the file is not found, start with an empty list

# Step 2: Define functions

# Function to add a new expense with category and date
def add_expense(amount, description, category):
    # Create a dictionary for the new expense with amount, description, category, and current date
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Record the current date and time
    }
    expenses.append(expense)  # Add the new expense to the list
    save_expenses()  # Save the updated list of expenses to the JSON file

# Function to view all expenses, with optional filtering by category or date
def view_expenses(filter_by=None, value=None):
    filtered_expenses = expenses  # Start with the full list of expenses
    # Filter by category if specified
    if filter_by == 'category':
        filtered_expenses = [expense for expense in expenses if expense['category'].lower() == value.lower()]
    # Filter by date if specified
    elif filter_by == 'date':
        filtered_expenses = [expense for expense in expenses if expense['date'].startswith(value)]
    
    # Calculate the total amount of filtered expenses
    total = sum(expense['amount'] for expense in filtered_expenses)
    
    # Display each expense in the filtered list
    for expense in filtered_expenses:
        print(f"Amount: ${expense['amount']}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")
    # Display the total expenses for the filtered list
    print(f"\nTotal Expenses: ${total}")

# Function to save expenses to the JSON file
def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)  # Save the expenses list with an indentation of 4 spaces for readability

# Step 3: Main loop
# Run a loop to repeatedly prompt the user for input
while True:
    # Display the menu options to the user
    print("\n1. Add Expense\n2. View All Expenses\n3. View Expenses by Category\n4. View Expenses by Date\n5. Exit")
    choice = input("Enter your choice: ")  # Get the user's choice

    # Handle the user's choice
    if choice == '1':
        # If the user chooses to add an expense
        try:
            amount = float(input("Enter amount: "))  # Prompt for the amount and convert it to a float
            description = input("Enter description: ")  # Prompt for the description of the expense
            category = input("Enter category: ")  # Prompt for the category of the expense
            add_expense(amount, description, category)  # Add the expense using the add_expense function
        except ValueError:
            print("Invalid amount. Please enter a number.")  # Handle invalid amount input
    elif choice == '2':
        # If the user chooses to view all expenses
        view_expenses()  # Display the list of all expenses
    elif choice == '3':
        # If the user chooses to view expenses by category
        category = input("Enter category to filter by: ")  # Prompt for the category to filter by
        view_expenses(filter_by='category', value=category)  # Display expenses filtered by the chosen category
    elif choice == '4':
        # If the user chooses to view expenses by date
        date = input("Enter date (YYYY-MM-DD) to filter by: ")  # Prompt for the date to filter by
        view_expenses(filter_by='date', value=date)  # Display expenses filtered by the chosen date
    elif choice == '5':
        # If the user chooses to exit
        break  # Exit the loop and end the program
    else:
        # If the user enters an invalid choice
        print("Invalid choice")  # Display an error message
