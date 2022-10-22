import math

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

D = (B**2)-(4*A*C)

if D < 0 or A == 0:
    print("Impossivel calcular")
else:
    D = math.sqrt(D)
    R1 = (-B + D)/(2*A)
    R2 = (-B - D)/(2*A)
    print("R1 = " "%.5f" % R1)
    print("R2 = " "%.5f" % R2)