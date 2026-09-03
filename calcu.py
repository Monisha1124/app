def calculate(a, b):
    print(f"Inputs: a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Division: {a} / {b} = {a / b}")
    else:
        print("Division: Cannot divide by zero")

if __name__ == "__main__":
    # Sample inputs for the calculator
    calculate(12, 4)
