class Triangle:
    def __init__(self):


        self.num = list(map(float, input("Enter 3 integer number:\n").split()))
        self.num.sort(reverse=True)
        self.a = self.num[0]
        self.b = self.num[1]
        self.c = self.num[2]

    def Invalid(self):
        if self.a >= self.b + self.c:
            print("Invalid")

    def Equailateral(self):
        if self.a == self.b == self.c:
            print("Equailateral")

    def Isosceles(self):
        if self.a == self.c or self.b == self.c or self.c == self.a:
            print("Isosceles.")

    def Scelene(self):
        if self.a != self.b or self.b != self.c or self.c != self.a:
            print("Scalene")

    def __del__(self):
        print("destruct")

obj = Triangle()
obj.Invalid()
obj.Equailateral()
obj.Isosceles()
obj.Scelene()
