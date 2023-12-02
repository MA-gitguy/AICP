print("\nEnter 1 to calculate area, perimeter and sum of angles of hexagon:")
print("Enter 2 to calculate area and perimeter of square:")
print("Press any other key to exit:\n")
selected_category = input()

cnic_id = ["1710172955523"]
cnic_last_digit = int(cnic_id[0][-1])
One_side_hex = cnic_last_digit
a = 120

def calcAngleSum(area_hex, Peri_hex):
    angle_sum = (6^2)*a
    print("Area of hexagon is:",area_hex,"\nPerimeter of hexagon is:", Peri_hex,"\nSum of angles of hexagon is:", angle_sum)
    

def calcPeri(area_hex):
    Peri_hex = 6*One_side_hex
    calcAngleSum(area_hex, Peri_hex)

def calcArea():
    area_hex = 1.5*1.732*One_side_hex
    calcPeri(area_hex)    

length_oneside_square = cnic_last_digit + 1

def calcPeriSquare():
    peri_square = length_oneside_square*4
    print("Perimeter of Square is:", peri_square)

def calcAreaSquare():
    area_square = length_oneside_square*2
    print("Area of Square is:", area_square)
    calcPeriSquare()


if selected_category == '1':
    calcArea()
elif selected_category == '2':
    calcAreaSquare()
else:
    quit()