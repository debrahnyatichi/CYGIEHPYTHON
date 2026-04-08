#Logical operators= evaluate multiple conditions(or, and, not)
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)

#OR CONDITION
temp = 20
is_raining = True

if temp >35 or temp <0 or is_raining:
    print ("The  Outdoor event is cancelled")
else:
    print (f"The Outdoor event is still Scheduled")

#AND
temp = 29
is_sunny = True

if temp >28 and is_sunny:
    print ("It is Hot outside 🥵")
    print ("It is SUNNY 🌞")
elif temp <=0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 😊")
    print("It is SUNNY 🌞")

#NOT
temp = 20
is_sunny = False
if temp >28 and not is_sunny:
    print ("It is Hot outside 🥵")
    print ("It is CLOUDY ☁️")
elif temp <=0 and not is_sunny:
    print("It is COLD outside ☁️")
    print("It is CLOUDY 🌞")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 😊")
    print("It is CLOUDY ☁️")