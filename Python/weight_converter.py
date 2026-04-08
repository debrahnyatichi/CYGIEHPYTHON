#python weight converter

weight = float(input("Enter your weight: "))
units = input("kilogram or pounds? (K or L): ")
if units == "K":
    weight *= 2.205
    units = "lbs."
    print (f"Your weight is: {round(weight, 1)} {units}")
elif units == "L":
    weight /= 2.205
    units = "Kgs."
    print (f"Your weight is: {round(weight, 1)} {units}")
else:
    print(f"{units} is not a valid unit")