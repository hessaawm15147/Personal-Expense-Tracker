import json  # Import the JSON module to handle saving and loading data

# Step 1: Load or initialize data
# Try to load existing expenses from 'expenses.json'
# If the file does not exist, initialize an empty list for expenses
try:
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)  # Load expenses from the JSON file
except FileNotFoundError:
    expenses = []  # If the file is not found, start with an empty list

# Step 2: Define functions

# Function to add a new expense
def add_expense(amount, description):
    # Append the new expense (amount and description) to the expenses list
    expenses.append({'amount': amount, 'description': description})
    save_expenses()  # Save the updated list of expenses to the JSON file

# Function to view all expenses
def view_expenses():
    # Loop through each expense in the expenses list and print it out
    for expense in expenses:
        print(f"Amount: ${expense['amount']}, Description: {expense['description']}")

# Function to save expenses to the JSON file
def save_expenses():
    # Write the expenses list to 'expenses.json', with an indentation of 4 spaces
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

# Step 3: Main loop
# Run a loop to repeatedly prompt the user for input
while True:
    # Display the menu options to the user
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Enter your choice: ")  # Get the user's choice

    # Handle the user's choice
    if choice == '1':
        # If the user chooses to add an expense
        amount = float(input("Enter amount: "))  # Prompt for the amount and convert it to a float
        description = input("Enter description: ")  # Prompt for the description of the expense
        add_expense(amount, description)  # Add the expense using the add_expense function
    elif choice == '2':
        # If the user chooses to view expenses
        view_expenses()  # Display the list of expenses
    elif choice == '3':
        # If the user chooses to exit
        break  # Exit the loop and end the program
    else:
        # If the user enters an invalid choice
        print("Invalid choice")  # Display an error message
