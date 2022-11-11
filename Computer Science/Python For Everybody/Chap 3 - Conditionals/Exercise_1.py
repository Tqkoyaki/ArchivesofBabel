# Write a program to prompt the user for hours
# and rate per hour using input to compute gross pay. Pay the
# hourly rate for the hours up to 40 and 1.5 times the hourly rate
# for all hours worked above 40 hours.
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

pay = 0
if hrs > 40:
    pay += (hrs - 40) * rate * 1.5
    hrs = 40
pay += hrs * rate

print(pay)