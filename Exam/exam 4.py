lst_number = list(map(int, input("Enter series of numbers with space: ").split()))
#for example lst_number = [1, 2, 3, 4]
running_sum = []
s = 0
for i in lst_number:
    s += i  # s = 0 and first i = lst_number[0], if i = 1 then s = 0 + 1 = 1, now s is 1 and i is 2, so s = 1+2 = 3, now s is 3 and i is 3, so s = 3+3= 6
    # print(s)
    running_sum.append(s)

print(running_sum)

"""
from itertools import accumulate
lst_number = list(map(int, input("Enter series of numbers with space: ").split()))
print(list(accumulate(lst_number)))
"""
