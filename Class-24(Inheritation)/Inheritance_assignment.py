class A:
    def funcA(self):
        print("I am a method of class 'A'")


class F:
    def funcF(self):
        print("I am a method class 'F'")


class C(A, F):
    def funcC(self):
        print("I am a child method of class of 'A' and 'F'")


class B(A):
    def funcB(self):
        print("I am a method of 'B'")


class D(B):
    def funcD(self):
        print("I am a child method of 'B'")


class E(B):
    def funcE(self):
        print("I am a child method of 'B'")



print("---------------------------------------------------")
print("We are objects of 'C' class (Multiple inheritance used).\n")
obj_C = C()
obj_C.funcA()
obj_C.funcF()
obj_C.funcC()
print("---------------------------------------------------")
print("We are objects of 'B' class (Single inheritance used).\n")
obj_B = B()
obj_B.funcA()
obj_B.funcB()
#obj_B.funcC()
#obj_B.funcF()

print("---------------------------------------------------")
print("We are objects of 'D' class (Multi/Hierarchical inheritance used).\n")
obj_D = D()
obj_D.funcB()
obj_D.funcD()
obj_D.funcA()

print("---------------------------------------------------")
print("We are objects of 'E' class (Multi/Hierarchical inheritance used).\n")
obj_E = E()
obj_E.funcB()
obj_E.funcA()
obj_E.funcE()
