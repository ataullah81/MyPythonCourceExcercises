test_case = int(input("How many times you would like loop: "))
start = 0
while start < test_case:
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num > 0:
        print("even positive")
    elif num % 2 != 0 and num < 0:
        print("odd negative")
    elif num == 0:
        print("null")
    elif num % 2 != 0 and num > 0:
        print("odd positive")
    elif num % 2 == 0 and num < 0:
        print("even negative")
    start += 1