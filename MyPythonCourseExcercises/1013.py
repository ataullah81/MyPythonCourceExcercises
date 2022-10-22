a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = int((a+b+abs(a-b))/2)
major_ab = int((d+c+abs(d-c))/2)
print(major_ab, "eh o maior")