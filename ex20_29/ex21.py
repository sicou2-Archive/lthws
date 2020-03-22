def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b 

def exponent(a, b):
    print(f"EXPONATING {a} ** {b}")
    return a ** b 

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(14, 2)
iq = divide(20, -2)
love = exponent(2, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}, Love: {love}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = exponent(love, add(age, subtract(height, multiply(weight, divide(iq, love)))))

print("What becomes: ", what, "Can you do it by hand?")