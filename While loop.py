"""
1. Python program to print ODD numbers from 1 to N using while loop.
2. Python program to print EVEN numbers from 1 to N using while loop.

3. Python program to print numbers from 1 to N using while loop.

4. Python Program to check entered number is ZERO, POSITIVE or NEGATIVE.

5. Python Program to find sum of first N natural number, N must be taken by the user.

6. Python program to print all even and odd numbers from 1 to N.
"""

# 1. Python program to print ODD numbers from 1 to N using while loop.

"""
start_point = int(input())
start = start_point
end_point = 0
while start_point > end_point:
    if start_point % 2 == 1:
        print(start_point)
    start_point -= 1



# -----------------------------------------
user_input = int(input())
start = 1
end = user_input
while start <= end:
    print(start)
    start += 2

#-----------------------------------------
#2. Python program to print EVEN numbers from 1 to N using while loop.


user_input = int(input())
start = 2
end = user_input
while start <= end:
    print(start)
    start += 2

# 3. Python program to print numbers from 1 to N using while loop.

user_input = int(input())
start = 1
end = user_input
while start <= end:
    print(start)
    start +=1
    

# 4. Python Program to check entered number is ZERO, POSITIVE or NEGATIVE.

test_case = int(input("How many times you would like to loop? "))
print("Your can test this case",user_input,"times.")
start = 1
end = test_case
while start <= end:
    num = int(input("Enter a number: "))
    if num == 0:
        print("You entered ZERO")
    if num > 0:
        print("You entered POSITIVE number")
    if num < 0:
        print("You entered NEGATIVE number")
    start += 1

# 5. Python Program to find sum of first N natural number, N must be taken by the user.

end_point = int(input())
start = 1
sum = 0
while start <= end_point:
    #print(start)
    sum += start # sum = sum + start
    start +=1
print(sum)


# Python program to print all numbers from 1 to N.
user_input = int(input())
start = 1
print("You want to know the list of numbers of {}.".format(user_input))
print("List of numbers from 1 to {} are:".format(user_input))
while start <= user_input:
    print(start, end=' ')
    start += 1

"""
# 6. Python program to print all even and odd numbers from 1 to N.
user_input = int(input())
print("You would like to know even and odd numbers of", user_input, ".")
start = 1
end = user_input
print("Even numbers of {} are:".format(user_input))
while start <= end:
    if start % 2 == 0:
        print(start, end=' ')
    start += 1

print("\nOdd numbers of {} are:".format(user_input))
start = 1
while start <= end:
    if start % 2 != 0:
        print(start, end=' ')
    start += 1
