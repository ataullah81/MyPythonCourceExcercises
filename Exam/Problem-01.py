user_input = list(map(int, input("Enter numbers: ").split()))

print("These numbers are divisible by 10.")
for i in range(len(user_input)):

    if user_input[i] % 10 == 0:
        print(user_input[i], end=' ')
    if user_input[i] >= 120:
        break
