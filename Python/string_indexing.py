#indexing: allows us to access elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

#start string
print(credit_number [6])

#end string: the start index is inclusive the ending index is exclusive
#print 1st 4digits of the string
print(credit_number [0:4])

print(credit_number [5:]) #prints from index 5 to the end of index
print(credit_number [-1]) #prints the last index of a string.
print(credit_number [-2])

#step string: access the characters in a string by a given step
print(credit_number [::3]) #counts every 3rd character in a string

#Create a program to get the last 4 digits of a number
last_digit = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")

#Reverse the characters in a string
credit_number = credit_number[:: -1] #to reverse a string you set the step to be -1
print(credit_number)
