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

#Exercise 3: calculate the circumference of a circle

import math

radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius
print(f" The circumference is: {round(circumference, 2)}cm")

#Exercise 4: calculate the area of a circle

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print(f" The area is: {round(area, 2)}cm^2")

# Exercise 5: Calculate the Hypotenuse of a right triangle
a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f" Answer is: {round(c, 2)} cm")
