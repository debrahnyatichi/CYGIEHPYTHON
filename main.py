#This is my first python program
print("I like Beef!")
print("It's really Good.")

#VARIABLES
#It is a container for a value(string, integer, float, boolean)
#It behaves as if it was the value it contains
#each variable should have a unique name.

#strings: they are in quotes
first_name = "cygieh"
food = "Beef"
email = "cygieh@fake.com"
print(first_name)
# f-string: to use formatted string literals, begin a string with f or F before opening quotes.
# Inside the string write a python expression  btn {} characters that can refer to variables or literal values.#
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

#integers: they are not in quotes, they are whole numbers.
age = 50
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float: they are decimal numbers
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is: ${price}")
print(f"Your gpa is: {gpa}")
print(f"Your ran {distance}km")

#Boolean: is either True or False T and F always caps.
is_student = True

print(f"Are you a student ? {is_student}")
#They are used internally.
if is_student:
    print("You are a student")
else:
        print("You are NOT a student")

for_sale = False
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT Available")

is_online = True
if is_online:
    print("You are online")
else:
    print("You are Offline")


#TYPECASTING:
#the process of converting a variable from one data type to another.
# str(), int(), float(), bool()

name= "cyber girl"
age = 30
gpa = 3.2
is_student = True

#you can get the data type of a variable by using type function:
type(name)
type(age)
type(gpa)
type(is_student)

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#Convert from 1 data type to another
gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

#can only concatenate str (not "int") to str

age += "1"
print(age)

name = bool(name)
print(name)

# input(): a function that prompts a user to enter data
# returns the entered data as a string

input("What is your name?: ")

#assign input to a variable
name = input("What is your name?: ")
age = input("How old are you?: ")

#you have to typecast int data type before concatenating it.
age = int(age)
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old")