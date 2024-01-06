# Constants
NUM_BOATS = 10
OPENING_HOUR = 10
CLOSING_HOUR = 17
HOURLY_RATE = 20
HALF_HOUR_RATE = 12

# Data structure to store boat information
boats_data = [{'hours_hired': 0, 'return_time': None} for _ in range(NUM_BOATS)]

# Task 1 - Calculate the money taken in a day for one boat
def calculate_daily_profit_one_boat(boat_number):
    print(f"\nBoat {boat_number}:")
    try:
        start_hour = int(input("Enter the starting hour (10-17): "))
        if not (OPENING_HOUR <= start_hour <= CLOSING_HOUR):
            print("Invalid starting hour. Boat can only be hired between 10:00 and 17:00.")
            return

        duration = float(input("Enter the duration in hours (0.5 or 1): "))
        if duration not in [0.5, 1]:
            print("Invalid duration. Please enter 0.5 or 1.")
            return

        # Calculate cost and update data
        cost = duration * (HALF_HOUR_RATE if duration == 0.5 else HOURLY_RATE)
        boats_data[boat_number - 1]['hours_hired'] += duration
        boats_data[boat_number - 1]['return_time'] = start_hour + duration

        print(f"Boat {boat_number} hired for {duration} hour(s). Cost: ${cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# Task 2 - Find the next boat available
def find_next_available_boat():
    current_hour = float(input("Enter the current hour: "))
    
    available_boats = [i + 1 for i, boat in enumerate(boats_data) if current_hour >= boat['return_time']]
    
    if not available_boats:
        next_available_time = min(boat['return_time'] for boat in boats_data)
        print(f"No boats available. Next available time: {next_available_time}")
    else:
        print(f"Available boats: {available_boats}")

# Task 3 - Calculate the money taken for all the boats at the end of the day
def calculate_daily_profit_all_boats():
    total_money_taken = sum(boat['hours_hired'] * (HALF_HOUR_RATE if boat['hours_hired'] == 0.5 else HOURLY_RATE) for boat in boats_data)
    total_hours_hired = sum(boat['hours_hired'] for boat in boats_data)
    unused_boats = sum(1 for boat in boats_data if boat['hours_hired'] == 0)

    most_used_boat = max(range(NUM_BOATS), key=lambda i: boats_data[i]['hours_hired'] if boats_data[i]['hours_hired'] > 0 else float('-inf')) + 1

    print("\nEnd of day report:")
    print(f"Total money taken: ${total_money_taken:.2f}")
    print(f"Total hours boats were hired: {total_hours_hired}")
    print(f"Number of boats not used: {unused_boats}")
    print(f"Boat {most_used_boat} was used the most with {boats_data[most_used_boat - 1]['hours_hired']} hours.")

# Test the tasks
for i in range(1, NUM_BOATS + 1):
    calculate_daily_profit_one_boat(i)

find_next_available_boat()
calculate_daily_profit_all_boats()
