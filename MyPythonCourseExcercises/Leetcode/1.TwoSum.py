nums = map(int, input().split())
number =list(nums)
print(type(number))
target = int(input())
isBreak = False
print(number)
for i in range(len(number)-1):
    if isBreak:
        break
    #print("this is i",i)
    for j in range(1, len(number)):
        #print("This is j",j)
        if int(number[i] + number[j]) == target:
            print([i,j])
            isBreak = True
            break