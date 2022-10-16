print("Enter a negative number to terminate.")
while True:
    numberOfCut = int(input("Number of cut: "))
    if numberOfCut < 0:
        break
    else:
        pizzaPieces = int(1 + numberOfCut * (numberOfCut + 1) / 2)
        print("You will get {} pizza slices.".format(pizzaPieces))
