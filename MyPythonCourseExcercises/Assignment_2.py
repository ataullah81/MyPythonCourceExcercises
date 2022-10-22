""""
2. Write a program in Python to check a given number is even or odd using the function.

Sample Input:
Input any number : 5

Expected Output :
The entered number is odd.
"""


def even_odd(num):
    if num % 2 == 0:
        return "The entered number is even."
    else:
        return "The entered number is odd."


number = int(input("Enter a number: "))
print(even_odd(number))
