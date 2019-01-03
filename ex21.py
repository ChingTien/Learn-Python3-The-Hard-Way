def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDE {a}/{b}")
    return a/b

print("let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"age:{age}, height:{height}, weight:{weight}, IQ:{iq}")