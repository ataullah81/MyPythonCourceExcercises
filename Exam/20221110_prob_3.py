end = float(input("How many times you want to loop: "))
start = 0
while start < end:
    start = int(input("Start range:"))
    end = int(input("End range: "))

    sum = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            sum += i
    print(sum)
    start += 1
