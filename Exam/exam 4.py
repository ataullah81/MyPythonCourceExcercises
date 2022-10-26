"""
lst_number = list(map(int, input("Enter series of numbers with space: ").split()))
running_sum = []
s = 0
for i in lst_number:
    s += i
    #print(s)
    running_sum.append(s)

print(running_sum)

"""
from itertools import accumulate
lst_number = list(map(int, input("Enter series of numbers with space: ").split()))
print(list(accumulate(lst_number)))