end = float(input("How many times you want to loop: "))
start = 0
while start < end:
    num = list(map(float, input("Enter 3 integer number:\n").split()))
    num.sort(reverse=True)
    a = num[0]
    b = num[1]
    c = num[2]
    if a >= b+c:
        print("Invalid")
    elif a == b == c:
        print("Equailateral")
    elif a == b or b == c or c ==a:
        print("Isosceles.")
    else:
        print("Scalene")
    start += 1




