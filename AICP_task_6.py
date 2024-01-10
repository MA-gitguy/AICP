# ..Task_6..


#Prices
CEMENT_PRICE = 3
GRAVEL_PRICE = 2
SAND_PRICE = 2
SPECIAL_PACK_PRICE = 10

def check_single_sack():
    print("Enter details for a single sack:")
    contents = input("Contents (C for cement, G for gravel, S for sand): ").upper()
    weight = float(input("Weight in kilograms: "))

    if contents in ('C', 'G', 'S'):
        if (contents == 'C' and 24.9 < weight < 25.1) or \
           (contents in ('G', 'S') and 49.9 < weight < 50.1):
            print(f"Accepted Sack - Contents: {contents}, Weight: {weight} kg")
            return weight
        else:
            print("Rejected Sack - Reasons:")
            if contents == 'C' and not (24.9 < weight < 25.1):
                print("  - Invalid weight for cement")
            elif contents in ('G', 'S') and not (49.9 < weight < 50.1):
                print("  - Invalid weight for gravel or sand")
    else:
        print("Rejected Sack - Reasons:")
        print("  - Invalid contents")

    return 0

def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))

    for _ in range(num_cement):
        result = check_single_sack()
        if result > 0:
            total_weight += result
        else:
            sacks_rejected += 1

    for _ in range(num_gravel):
        result = check_single_sack()
        if result > 0:
            total_weight += result
        else:
            sacks_rejected += 1

    for _ in range(num_sand):
        result = check_single_sack()
        if result > 0:
            total_weight += result
        else:
            sacks_rejected += 1

    print(f"Total order weight: {total_weight} kg")
    print(f"Sacks rejected from the order: {sacks_rejected}")

    return num_cement, num_gravel, num_sand  # Return the counts for Task 3


def calculate_order_price(num_cement, num_gravel, num_sand):
    regular_price = 0
    num_special_packs = 0

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
        print(f"Amount saved: ${discount_price}")
    else:
        print("No special packs in the order. No discount applied.")


order_counts = check_customer_order()
calculate_order_price(*order_counts)