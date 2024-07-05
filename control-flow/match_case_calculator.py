firstno = float(input("Enter the first number:"))

secondno = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case '+':
        ans = firstno + secondno
    case '-':
        ans = firstno - secondno
    case '*':
        ans = firstno * secondno
    case '/':
        if secondno !=0:
            ans = firstno / secondno
        else:
            print("invalid")
    case SyntaxError:
        print("input error")

    print(f"The result is {ans}")

