end = int(input("Enter a number: "))
print("Even numbers of {} are:".format(end))
for even in range(1, end+1):
    if even % 2 == 0:
        print(even, end=' ')
print("\n")
print("Odd numbers of {} are:".format(end))
for odd in range(1, end+1):
    if odd % 2 != 0:
        print(odd, end=' ')