# while loop: execute some code WHILE some condition remains true.

name = input("Enter your name: ")

while name == "":
    print("You did not enter a name")
    name = input("Enter your name: ")
print(f" Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = input("Enter your age: ") #helps to escape the while loop, without it the code will continuously run.
print(f"You are {age} years old")

#Example 2:

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

#Example 3: adding logical operatorsOR logical operator
num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print (f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")