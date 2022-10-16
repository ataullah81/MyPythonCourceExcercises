#1. Python program to print ODD numbers from 1 to N using for loop.
print("This is a odd number for loop.")
end = int(input("Enter a number to get odd number of it: "))
print("Odd numbers from 1 to {} are:".format(end))
for odd in range(1, end + 1):
    if odd % 2 != 0:
        print(odd, end=' ')
#2. Python program to print EVEN numbers from 1 to N using for loop.
print("\n")
print("This is a even number for loop.")
end = int(input("Enter a number to get even number of it: "))
print("Even numbers from 1 to {} are:".format(end))
for even in range(1, end + 1):
    if even % 2 == 0:
        print(even, end=' ')

#3. Python program to print numbers from 1 to N using for loop.
print("\n")
print("This is a for loop to print numbers.")
end = int(input("Enter a number: "))
print("Numbers from 1 to {} are:".format(end))
for number in range(1, end + 1):
    print(number, end=' ')
