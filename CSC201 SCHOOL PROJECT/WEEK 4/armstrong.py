#Code Objective is to use while loop to check for Armstrong number in certain interval

def is_armstrong(num):
    # Calculate the number of digits in num
    num_digits = len(str(num))
    
    # Initialize sum of powers to 0
    sum_of_powers = 0
    temp = num
    
    # Calculate sum of digits raised to the power of num_digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    
    # Check if num is an Armstrong number
    return num == sum_of_powers

# Define the interval
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

# Validate the interval
if start >= end:
    print("Invalid interval. Starting number should be less than the ending number.")
else:
    print("Armstrong numbers within the interval:")
    num = start
    while num <= end:
        if is_armstrong(num):
            print(num)
        num += 1
