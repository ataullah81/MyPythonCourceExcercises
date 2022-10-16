#4. Python Program to find sum of first N natural number, N must be taken by the user.

end = int(input("Enter a number: "))
sum = 0
print("Natural number of {} are: ".format(end))
for natural in range(1, end+1):
    sum += natural
    print(natural, end=' ')
print("\nSum of those natural number's:",sum)
