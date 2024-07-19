def safe_divide(numerator, denominator):
    try:
    
        self.numerator = numerator
        self.denominator = denominator
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Divisionby zero is not allowed."

    except ValueError:
        return "Error: Non-numeric input provided."

if __name__ == "__main__":
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide("b", 5))
    print(safe_divide(10, "c"))

