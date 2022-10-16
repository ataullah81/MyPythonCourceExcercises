A, B, C = input().split()

A1 = float(A)
B1 = float(B)
C1 = float(C)


n = 3.14159

triangle = (1/2)*(A1*C1)
radius = n*C1**2
trapezium = ((A1+B1)*C1)/2
squire = B1**2
rectangle = A1 * B1

print("TRIANGULO: " "%.3f" % triangle)
print("CIRCULO: " "%.3f" % radius)
print("TRAPEZIO: " "%.3f" % trapezium)
print("QUADRADO: " "%.3f" % squire)
print("RETANGULO: " "%.3f" % rectangle)
