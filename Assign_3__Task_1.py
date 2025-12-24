# Assignment 3 Task 1

# Calculate Factorial Using a Function 

# Define funtion as name factorial

def factorial(number):
    fact = 1
    for i in range (1,number+1):
        fact *= i
    return fact

# here before calling a function declare Variable To store user input 

usernum = (int(input("Eneter a Number : ")))
print(f"Factorial of {usernum} is : {factorial(usernum)}")
    
