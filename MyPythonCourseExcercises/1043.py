a, b, c = map(float, input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    perimeter = a+b+c
    print("Perimetro =", "%.1f" % perimeter)
else:
    area_trapezium = (a + b)*c/2
    print("Area =", "%.1f" % area_trapezium)
