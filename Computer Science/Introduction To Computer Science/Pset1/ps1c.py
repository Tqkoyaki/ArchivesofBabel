# Assumed variables
semi_annual_raise = 0.07
r = 0.04
down_payment = 0.25
total_cost = 1_000_000
months = 36

# Gets user input
annual_salary = float(input("Enter the starting salary: "))

# Calculated needed cost
total_cost *= down_payment

# Accuracy of the calculation
epsilon = 100

# Initial values for the search
low = 0
high = 10_000
guess = (high + low) // 2

# Controls how many times the loop runs
current_savings = 0

# Steps counter
steps = 0

# Loops until the guess is within the epsilon
while steps < 10000:
    # Adds temp variables to reset the salary
    temp_salary = annual_salary
    monthly_salary = temp_salary / 12
    
    # Finds the savings with the current guess
    for i in range(1, months):
        # Updates current savings
        current_savings += current_savings * (r / 12)
        current_savings += monthly_salary * (guess / 10_000)
        
        # Updates the monthly salary based on raise
        if i % 6 == 0:
            temp_salary += temp_salary * semi_annual_raise
            monthly_salary = temp_salary / 12
    
    # Updates steps
    steps += 1
    
    # Checks if the solution is within the epsilon
    if abs(current_savings - total_cost) <= epsilon:
        # Prints the results
        print("Best savings rate:", guess / 10_000)
        print("Steps in bisection search:", steps)
        break
    
    # Resets the current savings
    if current_savings < total_cost:
        low = guess
    else:
        high = guess
    
    # Updates the guess and current savings
    guess = (high + low) // 2
    current_savings = 0

# Checks if the solution was not found
if abs(current_savings - total_cost) > epsilon:
    print("It is not possible to pay the down payment in three years.")