startNum = 1
looping = int(input("Enter a number: "))
counter = 0
while True:
    if counter == looping:
        break
    for i in range(4):
        if startNum % 4 == 0:
            startNum += 1
            print()
        else:
            print(startNum, end=' ')
            startNum += 1
    counter += 1
