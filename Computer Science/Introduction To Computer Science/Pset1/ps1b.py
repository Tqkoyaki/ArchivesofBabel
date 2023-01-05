# Assumed parameters
portion_down_payment = 0.25
r = 0.04

# Counter variable holding savings and months
current_savings = 0
months = 0

# Parameters taken as input from user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Convert annual to monthly salary
monthly_salary = annual_salary / 12

# Updates total cost based on down payment
total_cost *= portion_down_payment

while current_savings < total_cost:
    # Updates months that went by
    months += 1
    
    # Updates current savings
    current_savings += current_savings * (r / 12)
    current_savings += monthly_salary * portion_saved
    
    # Updates the monthly salary based on raise
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

# Prints results
print("Number of months:", months)