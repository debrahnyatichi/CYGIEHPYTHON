#Exercise 1: Area of a Rectangle
#we will prompt the user to enter a width and length of a rectangle
#we can't multiply sequence by non-int of type 'str', we will have to typecast them, in this case to float

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f" The area is: {area}cm^2")

#Example 2: Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the Price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")