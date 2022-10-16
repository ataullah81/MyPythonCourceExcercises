nums = list(map(int, input().split()))
target = int(input())
sum = 0
isBreak = False
for i in range(len(nums) - 1):
    if isBreak:
        break
    for j in range(1, len(nums)):
        sum = nums[i]+nums[j]
        if sum == target:
            print([i,j])
            isBreak = True
            break
