class Calculator:
    mul = None
    sub = None
    div = None
    sum = None

    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None

    def addition(self, *num):
        self.sum = 0
        for x in num:
            self.sum += x
        print(self.sum)

    def subtraction(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.sub = self.num1 - self.num2 + self.num3
        print(self.sub)

    def multiplication(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.mul = self.num1 * self.num2
        print(self.mul)

    def division(self, num1, num2):
        try:
            self.num1 = num1
            self.num2 = num2
            self.div = self.num1 / self.num2
            print(self.div)
        except Exception:
            print("Division by zero is not possible.")

    def __del__(self):
        print("Destruct the object")



add = Calculator()
add.addition(1, 2, 5, 6)
sub = Calculator()
sub.subtraction(6, 3, 3)
mul = Calculator()
mul.multiplication(9, 3)
div = Calculator()
div.division(9, 0)



