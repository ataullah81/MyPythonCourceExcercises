"""
lst = [10, 20, 30]

Output:
30
20
10
"""

"""
1. start 
2. end 
3. condition for terminate 
4. counter [Increment(+)/Decrement(-)] 
"""

"""
1. start = len(lst)-1 # 3 - 1 = 2 
2. end = 0 
3. counter >= end
4. counter = start -= 1 
"""
lst = [1, 2, 3, 4, 5, 6]

start = len(lst) - 1 # 1
end = 0 # 2

while start >= end: # 3
    print(lst[start]) # 4
    start -= 1 # 5