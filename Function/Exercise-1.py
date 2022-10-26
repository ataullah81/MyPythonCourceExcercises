# Write a program to create a function that takes two arguments, name and age, and print their value.

def age_name(x, y):
    test = x, y
    return test


name = input()
age = int(input())
print(age_name(age,name))

