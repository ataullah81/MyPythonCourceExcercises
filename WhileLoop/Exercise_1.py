"""
1) Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

2) Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

3) Write a program in Python to read N numbers from the keyboard and find their sum and average


#1) Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

positive_number = True
sum = 0
while positive_number:
    num = int(input())
    if num >= 0:
        sum += num
    else:
        positive_number = False
        print("Your sum is:",sum)


#--------------------------------------------------------
num = 0
sum = 0
while num >= 0:
    num = int(input("Enter a number:"))
    if num >= 0:
        sum += num
        num += 1
    else:
        print(""sum)

#2) Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# loop do not work
counter = 0

while counter >= 0:
    name = str(input())
    if name != 'END':
        print(name)
        counter += 1
    if name == 'END':
        print("I am done")

# loop works

name = []
#print("Write END to terminate")
while name != 'END':
    print("Write END to terminate")
    #print(name)
    name = str(input("Write your name: "))
    if name != 'END':
        print("Your name is:",name)
    else:
        print("I am done")

"""

# 3) Write a program in Python to read N numbers from the keyboard and find their sum and average

sum = 0
counter = 0
while True:
    num = input()
    if num != 'end':
        sum += int(num)
        counter += 1
        average = sum / counter
    else:
        break
print("Sum:",sum)
print("Average:",average)