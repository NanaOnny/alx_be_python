def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): Specifies the operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float or str: The result of the arithmetic operation. If division by zero occurs, return a specific message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        try:
            result = num1 / num2
        except ZeroDivisionError:

            return "Error: Division by zero is undefined."

from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

