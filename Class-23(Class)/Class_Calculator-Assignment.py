class Calculator:

    def __init__(self):
        print("These are calculator objects.")

    def addition(self, *num):
        summation = 0
        for x in num:
            summation += x
        return summation

    def subtraction(self, num1, num2, num3):
        return num1 - num2 + num3

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

    def __del__(self):
        print("Calculator objects destructed.")


print("My nick name is Russell")

cal = Calculator()
print("This is for 'R'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal.addition(9, 3, 3)))
print("Result of subtraction is:", (cal.subtraction(5, 2, 3)))
print("Result of multiplication is:", (cal.multiplication(9, 3)))
try:
    print("Result of division is:", (cal.division(9, 2)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal1 = Calculator()
print("This is for 'u'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal1.addition(10, 5, 3, 10, 20, 30)))
print("Result of subtraction is:", (cal1.subtraction(15, 2, 6)))
print("Result of multiplication is:", (cal1.multiplication(11, 5)))
try:
    print("Result of division is:", (cal1.division(25, 7)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal2 = Calculator()
print("This is for 's'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal2.addition(41,5, 6, 9, 100)))
print("Result of subtraction is:", (cal2.subtraction(100, 6, 3)))
print("Result of multiplication is:", (cal2.multiplication(9, 3)))
try:
    print("Result of division is:", (cal2.division(9, 0)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal3 = Calculator()
print("This is for another 's'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal3.addition(100,200, 300,400)))
print("Result of subtraction is:", (cal3.subtraction(4, 10, 3)))
print("Result of multiplication is:", (cal3.multiplication(21, 4)))
try:
    print("Result of division is:", (cal3.division(55, 11)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal4 = Calculator()
print("This is for 'e'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal4.addition(5, 9, 11, 21, 22)))
print("Result of subtraction is:", (cal4.subtraction(66, 2, 55)))
print("Result of multiplication is:", (cal4.multiplication(9, 3)))
try:
    print("Result of division is:", (cal4.division(8, 9)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal5 = Calculator()
print("This is for 'l'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal5.addition(25, 9, 3, 3, 85)))
print("Result of subtraction is:", (cal5.subtraction(6, 2, 3)))
print("Result of multiplication is:", (cal5.multiplication(8, 3)))
try:
    print("Result of division is:", (cal5.division(8, 2)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")

cal6 = Calculator()
print("This is for another 'l'")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")

print("Result of addition is:", (cal6.addition(9, 9, 9, 9)))
print("Result of subtraction is:", (cal6.subtraction(5, 9, 3)))
print("Result of multiplication is:", (cal6.multiplication(15, 6)))
try:
    print("Result of division is:", (cal6.division(26, 2)))
except Exception:
    print("Division by zero is not possible.")
print("-----------------------------------------------------\n")
