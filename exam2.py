num = int(input())
start = 0
while start > num:
    x = int(input())
    y = int(input())
    if y % 2 == 1:
        y += 1
    print(y)