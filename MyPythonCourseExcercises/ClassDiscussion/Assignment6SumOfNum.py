import sys

sumOfNum = 0
for i in range(sys.maxsize ** 10):
    num = int(input())
    if num < 0:
        break
    sumOfNum += num

print(sumOfNum)
