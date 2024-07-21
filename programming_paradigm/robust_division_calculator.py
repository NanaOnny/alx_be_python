def safe_divide(numerator, denominator):
    try:
        a = float(numerator)
        b = float(denominator)

        result = a / b

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

    return f"The result of the division is {result}"
