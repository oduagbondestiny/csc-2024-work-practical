#program objective is to create a program that find the factorial of a give nnumber provided by the user

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)