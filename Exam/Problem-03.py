test_case = int(input("How many times you would like loop: "))
start = 0
while start < test_case:
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num > 0:
        print("even positive")
    if num % 2 != 0 and num < 0:
        print("odd negative")
    if num == 0:
        print("null")
    if num % 2 != 0 and num > 0:
        print("odd positive")
    if num % 2 == 0 and num < 0:
        print("even negative")
    start += 1