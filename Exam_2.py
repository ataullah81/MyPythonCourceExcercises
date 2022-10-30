n = int(input())
for i in range(n):
    num, num1 = map(int, input().split())
    sum = 0
    cnt = 0
    while True:
        if cnt == num1:
            break
        if num % 2 == 1:
            print(num)

            cnt += 1
            sum += num

        num += 1
    print(sum)

