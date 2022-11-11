# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay.
hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

gross = hrs * rate

print("Pay:", gross)