# if = used to do some code only IF some condition is True else do something else
#it is for decision making
from main import for_sale

age = int(input("Enter the age: "))

#let's assume a user will like to sign up for credit card, but to do so he has to be equal to OR over 18 years
if age >100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
elif age >100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")

response = input("Would you like have food? (yes/no): ")

if response.lower() == "yes":
    print("Have some food!")
else:
    print("No food for you.")


name = input("What is your name? ")
if name == "":
    print("Name is empty")
else:
    print(f"Hello {name} ")

#use of boolean with if statements
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = False
if online:
    print("The user is online")
else:
    print("The user is offline")