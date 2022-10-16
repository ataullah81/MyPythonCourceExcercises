"""
A = float(input("Enter a product value: " ))
B = float(input("Enter another product value: " ))
C = float(input("Enter one more product value: " ))
D = float(input("Enter more product value: " ))
dif = (A * B - C * D)
#print ("DIFFERENCE =",dif)

print("DIFFERENCE = {}" .format("%.2f"%dif))
"""
float1 = 2.154327
format_float = "{:.1f}".format(float1)

print(format_float)
print (type(format_float))
float2 = float(format_float)
print (type(float2))


unit_price2 = float(input("unit price").format(":.2f"))
print(unit_price2)
print (type(unit_price2))

A = "{:.2f}".format(float(input()))
print(A)
print(type(A))