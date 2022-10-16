#end = float(input("How many times you want to loop: "))
#start = 0
#while start < end:
num = list(map(float, input().split()))
num.sort(reverse=True)
a = num[0]
b = num[1]
c = num[2]
if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
if a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
if a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or c ==a:
    print("TRIANGULO ISOSCELES")
    #start += 1




