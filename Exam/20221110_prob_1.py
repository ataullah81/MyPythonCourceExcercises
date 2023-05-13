try:
    inp = list(map(int, input("Enter number with space:\n").split()))
    lst2 = []
    for i in inp:
        lst2.append(i)
    print("Ans=",inp + lst2)
except Exception:
    print("Enter valid number.")
