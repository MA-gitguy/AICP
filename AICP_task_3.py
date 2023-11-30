print("Student ID is XY12345678")

print("\nEnter 1 to display the bill of slab 1 and slab 2.")
print("Enter 2 to display the bill of slab 3.")
print("Press any other key to exit.\n")
selected_slab = input("Enter Your Choice: \n")


slab_1_2_3 = [[55, 65, 75], [120, 150, 170], [210, 230, 240]]

def costslab1():
    slab_1_price = []
    for units in slab_1_2_3[0]:
        price_slab_1 = units*10
        slab_1_price.append(price_slab_1)
    print("Bill for Slab 1 is: ")
    print(slab_1_price)

def costslab2():
    slab_2_price = []
    for units in slab_1_2_3[1]:
        price_slab_2 = units*10
        slab_2_price.append(price_slab_2)
    print("Bill for Slab 2 is: ")
    print(slab_2_price)


def costslab3():
    slab_3_price = []
    for units in slab_1_2_3[2]:
        price_slab_3 = units*10
        slab_3_price.append(price_slab_3)
    print("Bill for Slab 3 is: ")
    print(slab_3_price)

if selected_slab == '1':
    costslab1()
    costslab2()
elif selected_slab == '2':
    costslab3()
else:
    quit()




    

