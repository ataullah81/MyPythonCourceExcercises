# 10. Printing all letters except some using Python while loop

word = "Bangladesh"
#print all except l
start = 0
while start < len(word):
    if word[start] == "l":
        start += 1
        continue

    print(word[start],end = ' ')
    start +=1

#18. Finding the factorial of a given number using while loop

start = 0
num = int(input())
while num != 0:
    
    if