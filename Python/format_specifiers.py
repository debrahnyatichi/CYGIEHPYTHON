#format specifiers:
#When used in the context of an f string {value:flags} they allow us to format a value based on what flags are inserted.
# :.number(f)= round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03= allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = centre align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 30000.14159
price2 = -98700.65
price3 = 12000.34

# :.number(f)= round to that many decimal places (fixed point):
# each output now has 2decimal places
print(f"Price 1 is: ${price1:.2f}")
print(f"Price 2 is: ${price2:.2f}")
print(f"Price 3 is: ${price3:.2f}")

# :(number) = allocate that many spaces:
# each output has a value of 10 spaces to display the output
print(f"Price 1 is: ${price1:10}")
print(f"Price 2 is: ${price2:10}")
print(f"Price 3 is: ${price3:10}")

# :03= allocate and zero pad that many spaces
#each number will be 0 padded
print(f"Price 1 is: ${price1:010}")
print(f"Price 2 is: ${price2:010}")
print(f"Price 3 is: ${price3:010}")

# :< = left justify: each value is left justified(each value aligns to the left and all the space after, they are all uniform)
print(f"Price 1 is: ${price1:<10}")
print(f"Price 2 is: ${price2:<10}")
print(f"Price 3 is: ${price3:<10}")

# :> = right justify:
print(f"Price 1 is: ${price1:>10}")
print(f"Price 2 is: ${price2:>10}")
print(f"Price 3 is: ${price3:>10}")

# :^ = centre align: numbers are centred
print(f"Price 1 is: ${price1:^10}")
print(f"Price 2 is: ${price2:^10}")
print(f"Price 3 is: ${price3:^10}")

# :+ = use a plus sign to indicate positive value:
# any +ve number is preceded with a + sign and any -ve is preceded with the - sign
print(f"Price 1 is: ${price1:+}")
print(f"Price 2 is: ${price2:+}")
print(f"Price 3 is: ${price3:+}")

# : = insert a space before positive numbers
print(f"Price 1 is: ${price1: }")
print(f"Price 2 is: ${price2: }")
print(f"Price 3 is: ${price3: }")

# :, = comma separator: a thousand separator
print(f"Price 1 is: ${price1:,}")
print(f"Price 2 is: ${price2:,}")
print(f"Price 3 is: ${price3:,}")

# := = place sign to leftmost position
print(f"Price 1 is: ${price1:=}")
print(f"Price 2 is: ${price2:=}")
print(f"Price 3 is: ${price3:=}")