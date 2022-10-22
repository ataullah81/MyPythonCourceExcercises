num = int(input("How many Numbers you want :"))

i=0
Count = 0
while(Count != num):
    if((i%3==0) and (i%5==0)):
        Count += 1
        print()
    i = i + 1

print("Count is :",Count)