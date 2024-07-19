def safe_divide(numerator, denominator):
    try:
    
        num = float( numerator)
        denom = float( denominator)
        result = num / denom
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Non-numeric input provided."

if __name__ == "__main__":
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide("b", 5))
    print(safe_divide(10, "c"))

