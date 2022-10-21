start =1
end = int(input())
while start <= end:
    if start % 4 ==0:
        start +=1
        print(start)
       # continue
    else:
        print(start,end = ' ')
        start +=1