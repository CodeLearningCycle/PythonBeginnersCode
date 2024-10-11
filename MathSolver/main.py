def MathSolver():
    while True:
        try:
            a = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            b = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        operator = input("Enter the operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Please enter a valid operator!")
        
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            print("Division by zero is not allowed!")
            return

    print("The solve of the two numbers is:", result)

MathSolver()