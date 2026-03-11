# Interest: the monetary charge for privilege of borrowing money.
# # A= P(1+r/n)^t
# A = final amount
# P = initial principle amount
# r = interest rate
# t = number of time of periods elapsed

principle = 0
rate = 0
time = 0

#Principle
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")


#rate
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest can't be less than or equal to zero")


#time
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

#calculate the interest
total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
print(principle)
print(rate)
print(time)