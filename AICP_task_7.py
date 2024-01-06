# Constants
NUM_CHARITIES = 3

# Task 1 - Set up the donation system
charities = []
for i in range(NUM_CHARITIES):
    charity_name = input(f"Enter the name of Charity {i + 1}: ")
    charities.append(charity_name)

# Display charity names with corresponding numbers
for i, charity in enumerate(charities, start=1):
    print(f"{i}. {charity}")

# Initialize totals
charity_totals = [0] * NUM_CHARITIES

# Task 2 - Record and total each donation
def record_donation():
    while True:
        try:
            choice = int(input("Enter the charity choice (1, 2, 3) or -1 to show totals: "))
            if choice == -1:
                break
            elif 1 <= choice <= NUM_CHARITIES:
                bill_amount = float(input("Enter the customer's shopping bill amount: "))
                donation = bill_amount * 0.01
                charity_totals[choice - 1] += donation
                print(f"Donation of ${donation} recorded for {charities[choice - 1]}")
            else:
                print("Invalid charity choice. Please enter 1, 2, 3, or -1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Task 3 - Show the totals so far
def show_totals():
    print("\nCharity Totals:")
    for i, charity in enumerate(charities):
        print(f"{charity}: ${charity_totals[i]:.2f}")

    grand_total = sum(charity_totals)
    print("\nGRAND TOTAL DONATED TO CHARITY: ${:.2f}".format(grand_total))

# Test the tasks
record_donation()
record_donation()
record_donation()
show_totals()
