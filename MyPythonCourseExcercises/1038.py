"""
x, y = map(int, input().split())
print(type(x))
"""
x, y = map(int, input().split())

if x == 1:
    price = y * 4.00
    print("Total: R$", "%.2f" % price)
elif x == 2:
    price = y * 4.50
    print("Total: R$", "%.2f" % price)
elif x == 3:
    price = y * 5.00
    print("Total: R$", "%.2f" % price)
elif x == 4:
    price = y * 2.00
    print("Total: R$", "%.2f" % price)
elif x == 5:
    price = y * 1.50
    print("Total: R$", "%.2f" % price)