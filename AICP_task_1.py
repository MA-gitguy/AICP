#      Online Computer Store

M_comp = [
    {"Category": "Case", "Type": ["A1. Compact" ,"A2. Tower"], "Price": {"A1": 75.00, "A2": 150.00}},
    {"Category": "RAM", "Type": ["B1. 8GB", "B2. 16GB", "B3. 32GB"], "Price": {"B1": 79.00, "B2": 149.00, "B3": 299.99}},
    {"Category": "Main Hard Disk Drive", "Type": ["C1. 1TB", "C2. 2TB", "C3. 4TB"], "Price": {"C1": 49.99, "C2": 89.99, "C3": 129.99}}
]

A_comp = [
    {"Category": "Solid State Drive", "Type": ["D1. 240GB", "D2. 480GB", "N. Next"], "Price": {"D1": 59.99, "D2": 199.99}},
    {"Category": "Second HDD", "Type": ["E1. 1TB", "E2. 2TB", "E3. 4TB", "N. Next"], "Price": {"E1": 49.99, "E2": 89.99, "E3": 129.99}},
    {"Category": "Optical Drive", "Type": ["F1. DVD/Blu-Ray Players", "F2. DVD/Blu-Ray Writer", "N. Next"], "Price": {"F1": 50.00, "F2": 100.00}},
    {"Category": "Operating System", "Type": ["G1. Standard Version", "G2. Professional Version", "N. Next"], "Price": {"G1": 100.00, "G2": 175}}
]

def main_component(category, Type, price):
    print("\nItem: ", category)
    print("Types: ", Type)
    print("Price: ", price)
    y = input("Select one Type: ")
    return y.upper()

def discount(x, Pri_1, Pri_2):
    Total_Price = Pri_1 + Pri_2
    if x >= 0 & x<1:
        Discount = Total_Price*5/100
        Total_Price = Total_Price - Discount
        print("Your Total Price of computer with 5% Discount is: ", Total_Price)
    else:
        Discount = Total_Price*10/100
        Total_Price = Total_Price - Discount
        print("Your Total Price of computer with 10% Discount is: ", Total_Price)   


def main():
    Pri_1 = 0
    for component in M_comp:
        selected_type = main_component(component["Category"], component["Type"], component["Price"])
        P1 = component["Price"][selected_type]
        Pri_1 = Pri_1+P1
        print("\nTotal Price of Basic components: " ,Pri_1)
    Pri_2 = 0
    x = 0
    ask = input("Do you want to see some additional items to buy: \ny/n: ")
    ask = ask.upper()
    if ask == "Y":
        for component in A_comp:
            selected_type = main_component(component["Category"], component["Type"], component["Price"])
            if selected_type.upper() == "N":
                next
            else:
                x = x+1
                P2 = component["Price"][selected_type]
                Pri_2 = Pri_2+P2
            discount(x, Pri_2, Pri_1)
    else:
        print("Thank You for Shopping")

    
    
        

main()