user_input = list(map(int, input("Enter numbers: ").split()))
start = 0
while True:
    if user_input[i] >= 120:
        break
    if user_input[i] % 10 == 0:
        print(user_input[i], end=' ')
        start += 1