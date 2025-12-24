# Assignment 3 Task 2
# Using The Math Module For Calculation 

# using the math Module For calculation  square root | Natural logarithm Log base e | in radians |


def Calculation(number):
    import math
    sr = math.sqrt(number)
    log = math.log(number)
    rad = math.sin(number)
    return sr,log,rad     
    
usernum = float(input("Eneter a Number : "))

sr ,log , rad = Calculation(usernum)   

print(f"Square root : {sr}") 
print(f"Logarithm : {log}") 
print(f"Sine : {rad}") 
