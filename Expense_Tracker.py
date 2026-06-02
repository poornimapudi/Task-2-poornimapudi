# Expense Tracker Program

# Variable to store the total amount spent
total_spent = 0

# Variable to count how many expenses are entered
expense_count = 0

# Display heading for the user
print("========== Expense Tracker ==========")
print("Enter your daily expenses.")
print("Type 'done' when you have finished.\n")

# Keep asking for expenses until the user types 'done'
while True:

    # Take input from the user
    amount = input("Enter expense amount: ")

    # Check if the user wants to stop entering expenses
    if amount.lower() == "done":
        break

    try:
        # Convert the input into a number
        amount = float(amount)

        # Prevent negative or zero values
        if amount <= 0:
            print("Expense amount must be greater than 0.\n")
            continue

        # Add the expense to the running total
        total_spent += amount

        # Increase the expense counter by 1
        expense_count += 1

        # Show confirmation message
        print(f"Expense Added: {amount:.2f}")

        # Show updated total after each entry
        print(f"Current Total: {total_spent:.2f}\n")

    # Handle invalid inputs such as text or symbols
    except ValueError:
        print("Please enter a valid amount.\n")

# Display summary only if at least one expense was entered
if expense_count > 0:

    # Calculate average expense
    average_expense = total_spent / expense_count

    print("\n========== Expense Summary ==========")

    # Show total number of expenses
    print(f"Number of Expenses : {expense_count}")

    # Show total amount spent
    print(f"Total Spent        : {total_spent:.2f}")

    # Show average spending per transaction
    print(f"Average Expense    : {average_expense:.2f}")

else:
    # Message when no expenses are entered
    print("\nNo expenses were recorded.")