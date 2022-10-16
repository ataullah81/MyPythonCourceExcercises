""""
1. Write a program in Python to find the square of any number using the function.

Sample Input:
Input any number for square : 20

Expected Output :
The square of 20 is : 400.00

"""


def find_square(num):
    square = num ** 2
    return square


number = int(input("Enter any number for square: "))
print("The square of {} is:".format(number), find_square(number))
