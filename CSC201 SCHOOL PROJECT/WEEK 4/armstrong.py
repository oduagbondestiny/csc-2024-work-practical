#Code Objective is to use while loop to check for Armstrong number in certain interval

def armstrong(num):

    # Calculate the number of digits in num
    num_digits = len(str(num))
    
    # Initialize sum of powers to 0, create a temp veriable to sure num, and a list strong
    sum_of_powers = 0
    temp = num
    Strong = []
    
    # Calculate sum of digits raised to the power of num_digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10

        Strong.append(f"{digit} ^ {num_digits}")

    
    print(f"The n: {num_digits}")
    print(f"{num} ={Strong}  which is = {sum_of_powers}")

    # Check if num is an Armstrong number
    if num == sum_of_powers:

        print("\nThis Number is an ArmStrong Number")

    else:

        print("\nThis Number is not an ArmStrong Number")
    

# collect user input as interger 
number = int(input("Enter the number of the interval: "))

print("Armstrong numbers within the interval:")
armstrong(number)
        
