import sys

def addition(a,b):
    addition = a + b
    return addition

def subtraction(a,b):   
    subtraction = a - b
    return subtraction

def multiplication(a,b):
    multiplication = a * b
    return multiplication

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "addition":
    output = addition(a,b)
    print(output)

elif operation == "subtraction":   
    output = subtraction(a,b)
    print(output)

elif operation == "multiplication":
    output = multiplication(a,b)
    print(output)

else:
    print("unknown operation")

