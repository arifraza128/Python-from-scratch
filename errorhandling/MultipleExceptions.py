try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    print(a / b)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Division by zero is not allowed")
