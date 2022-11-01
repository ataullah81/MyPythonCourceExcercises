# Provided a list where every element occurs doubled except for one. Find that single one.
isContinue = True
start = 0
while isContinue:
    given_lst = list(map(int, input("Enter numbers with space: \n").split()))
    single_value = []
    for i in given_lst:
        # checking elements in list, which is not exist more than one time
        if given_lst.count(i) < 2:
            single_value.append(i)
    print("Unique value:", single_value, sep='\n')
    inp = input("Write 'ok' to continue and 'no' to terminate: \n")
    if inp == 'ok':
        continue
    elif inp == 'no':
        break
start += 1
