#6. Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
#While loop
sum = 0
start = 0
print("Enter a negative number to terminate.")
while start >= 0:
    num = int(input("Enter a positive number: "))
    if num > 0:
        sum += num
        start += 1
    else:
        print("Sum of the entered number is:",sum)