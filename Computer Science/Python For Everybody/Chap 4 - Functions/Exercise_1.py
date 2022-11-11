# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay should be the normal rate
# for hours up to 40 and time-and-a-half for the hourly rate for all
# hours worked above 40 hours. Put the logic to do the computation of
# pay in a function called computepay() and use the function to do the
# compuation. The function should return a value.
def computepay(hrs, rate):
    pay = 0
    if hrs > 40:
        pay = (hrs - 40) * 1.5 * rate
        hrs = 40
    return hrs * rate + pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

print("Pay", computepay(hrs, rate))