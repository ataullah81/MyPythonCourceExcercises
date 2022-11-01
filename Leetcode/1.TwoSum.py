nums = list(map(int, input().split()))

#print(type(nums))
target = int(input())
isBreak = False
print(nums)
for i in range(len(nums)-1):
    if isBreak:
        break
    #print("this is i",i)
    for j in range(1, len(nums)):
        #print("This is j",j)
        if int(nums[i] + nums[j]) == target:
            print([i,j])
            isBreak = True
            break