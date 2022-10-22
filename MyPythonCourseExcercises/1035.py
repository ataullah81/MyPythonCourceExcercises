A, B, C, D = input().split()
A1 = int(A)
B1 = int(B)
C1 = int(C)
D1 = int(D)
if B1 > C1 and D1 > A1 and (C1+D1) > (A1+B1) and C1 > 0 and D1 > 0 and A1 % 2 == 0:

    print("Valores aceitos")

else:

    print("Valores nao aceitos")