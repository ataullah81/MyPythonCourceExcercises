# 1) Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
import sys

sum = 0
while True:
    num = int(input())
    if num < 0:
        break
    else:
        sum += num
print(sum)

#For loop
import sys
sum = 0
for i in range(sys.maxsize):
    num = int(input())
    if num < 0:
        break
    else:
        sum += num
print(sum)