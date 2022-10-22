"""

a + b > c and b + c > a and c + a > b -> Valid Triangle -> else -> not valid

3

1 1 1 -> valid
1 2 3 -> Invalid

a
b
c

# Conditional Logic ->
2

a b c -> Valid
a b c -> Invalid

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
num_of_test_case = int(input("How many times you want to run this: "))

start = num_of_test_case
stop = 0

while start > stop:
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    if (a + b > c) and (b + c > a) and (c + a > b):
        print("Triangle is valid.")
    else:
        print("Triangle is invalid.")
    start -= 1
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
"""
num_of_test_case = int(input("Enter a number you want to loop this program: "))
print("You can loop (", num_of_test_case, ") times.")

start = num_of_test_case
stop = 0

while start > stop:
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    if (a + b > c) and (b + c > a) and (c + a > b):
        print("Triangle is valid.")
    else:
        print("Triangle is invalid.")
    start -= 1
    if start >= 1:
        print("You have (", start, ") times left.")
    else:
        print("You finished your looping, bye bye!")
