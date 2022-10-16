# 8. Write a program in Python to read N numbers from the keyboard and find their sum and average
import sys
sum = 0
for n in range(sys.maxsize):
    num = input()
    if num == 'ok':
        break
    else:
        sum += int(num)
print(sum)
print(sum/n)
"""
sum = 0
counter = 0
while True:
    num = input()
    if num == 'ok':
        break
    else:
        sum += int(num)
        counter +=1
print(sum)
print(sum/counter)
"""