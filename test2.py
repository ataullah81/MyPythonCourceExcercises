
start = 1
isContinue = True
counter = 0
inp = int(input())
while isContinue:
    if counter == inp:
        break
    if start % 4 == 0:
        print()
        continue
    else:
        print(start,end = ' ')

        start +=1
        counter -= 1
#isContinue = False