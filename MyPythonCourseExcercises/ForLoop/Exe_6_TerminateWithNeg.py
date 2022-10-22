#6. Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
# For loop
import sys
sum = 0
for n in range(sys.maxsize):
    num = int(input("Enter a number: "))
    if num < 0:
        break
    else:
        sum += int(num)
print("Sum of enetered number is:",sum)


"""
#While loop
sum = 0
num = 0
print("Enter a negative number to terminate.")
while num >= 0:
    num = int(input("Enter a positive number: "))
    if num > 0:
        sum += num
        num += 1
    else:
        print("Sum of the entered number is:",sum)
"""
