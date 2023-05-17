def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter operation number (1-4): ")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == '1':
        result = num1 + num2
        print("Result:", result)
    elif operation == '2':
        result = num1 - num2
        print("Result:", result)
    elif operation == '3':
        result = num1 * num2
        print("Result:", result)
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operation")

        # I took this on chatgpt
        