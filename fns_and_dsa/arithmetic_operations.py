def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."

if __name__ == "__main__":
    print(perform_operation(6, 3, 'add'))
    print(perform_operation(6, 3, 'subtract'))
    print(perform_operation(6, 3, 'multiply'))
    print(perform_operation(6, 3, 'divide'))
    print(perform_operation(6, 0, 'divide'))
    print(perform_operation(6, 3, 'modulus'))
