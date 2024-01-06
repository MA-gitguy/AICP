# Constants
CEMENT_PRICE = 3
GRAVEL_PRICE = 2
SAND_PRICE = 2
SPECIAL_PACK_PRICE = 10

# Task 1 - Check a single sack
def check_single_sack():
    print("Enter details for a single sack:")
    contents = input("Contents: \nC for cement \nG for gravel \nS for sand: ")
    contents = contents.upper()
    weight = float(input("Weight in kilograms: "))
    

    if (contents == 'C' and 24.9 < weight < 25.1) or \
       (contents in ('G', 'S') and 49.9 < weight < 50.1):
        print(f"Accepted Sack - Contents: {contents}, Weight: {weight} kg")
    else:
        print("Rejected Sack - Reasons:")
        if contents not in ('C', 'G', 'S'):
            print("  - Invalid contents")
        if contents == 'C' and not (24.9 < weight < 25.1):
            print("  - Invalid weight for cement")
        elif contents in ('G', 'S') and not (49.9 < weight < 50.1):
            print("  - Invalid weight for gravel or sand")
    return weight

# Task 2 - Check a customer's order
def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))

    for _ in range(num_cement):
        result = check_single_sack()
        if result == "Rejected":
            sacks_rejected += 1
        else:
            total_weight += float(result)

    for _ in range(num_gravel):
        result = check_single_sack()
        if result == "Rejected":
            sacks_rejected += 1
        else:
            total_weight += float(result)

    for _ in range(num_sand):
        result = check_single_sack()
        if result == "Rejected":
            sacks_rejected += 1
        else:
            total_weight += float(result)

    print(f"Total order weight: {total_weight} kg")
    print(f"Sacks rejected from the order: {sacks_rejected}")

# Task 3 - Calculate the price for a customer's order
def calculate_order_price():
    regular_price = 0
    num_special_packs = 0

    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))

    regular_price += num_cement * CEMENT_PRICE
    regular_price += num_gravel * GRAVEL_PRICE
    regular_price += num_sand * SAND_PRICE

    num_special_packs = min(num_cement, num_gravel // 2, num_sand // 2)
    discount_price = num_special_packs * SPECIAL_PACK_PRICE
    total_price = regular_price - discount_price

    print(f"Regular price for the order: ${regular_price}")
    if num_special_packs > 0:
        print(f"Discount price for {num_special_packs} special pack(s): -${discount_price}")
        print(f"New price for the order: ${total_price}")
    else:
        print("No special packs in the order. No discount applied.")

# Test the tasks
check_single_sack()
check_customer_order()
calculate_order_price()
