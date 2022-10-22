numbers = list(map(int, input().split()))
target = int(input())
isBreak = False
for i in range(len(numbers) - 1):
    if isBreak:
        break
    for j in range(1, len(numbers)):
       # print(f"{i},{j}",i,j)
        if numbers[i] + numbers[j] == target:
            print([i, j])
            isBreak = True
            break


