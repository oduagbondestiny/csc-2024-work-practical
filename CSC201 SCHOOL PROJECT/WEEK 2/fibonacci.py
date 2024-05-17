#program objective is to write a program to display the Fibonacci squence up to the nth
#where n is provided by the user 

def fibonacci(number):
    a, b =0,1

    #check if user inputed an int

    if isinstance(number, int):

        for _ in range(number):

            yield a

            a, b = b,a +b 

    else:

        print("Please Input an Integer")

#collecting user input
n= input("Input A Number:")

print ("Fibonacci sequence up to the", n, "termm(s):", list(fibonacci(n)))