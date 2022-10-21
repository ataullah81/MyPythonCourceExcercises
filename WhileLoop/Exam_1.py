a = 1
inp = int(input())
counter = 0
while True:
    if counter == inp:
        break
    for i in range(4):
        if a % 4 == 0:
            a = a+1
            print()
        else:
            print(a,end = ' ')
            a = a+1
    counter +=1