"""

start = 0
end = 3
terminate condition ->
counter

"""

"""
numOfTestCases = int(input())  # 3

start = 0
end = numOfTestCases - 1

while start <= end:

    # Block of Code - Start
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    # Block of Code - End

    start += 1

# Assignment

"""
"""

numOfTestCases = int(input())
start = numOfTestCases
end = 0
while start > end:
    num1 = int(input())
    num2 = int(input())
    print(num1+num2)
    start -= 1
    
"""
num_test_case = int(input("How many time you would like to loop: "))
print("You would like to loop (", num_test_case, ") times.")
start = 0
while start < num_test_case:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1+num2)
    start +=1

    if num_test_case > start:
        print("You have (",num_test_case - start,") times left.")
    else:
        print("You finished your looping, bye bye!!")