class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

calc = Calculator()

print("Sum of 2 numbers:", calc.add(5, 10))
print("Sum of 3 numbers:", calc.add(1, 2, 3))
