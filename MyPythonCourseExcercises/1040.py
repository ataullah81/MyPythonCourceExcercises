n1,n2,n3,n4 = list(map(float,input().split()))
# n1, n2, n3, n4 = map(float, input().split())
average = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)
print("Media:", "%.1f" % average)
if average > 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
elif average >= 5.0 and average < 7:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame:", "%.1f" % n5)
    average2 = (n5+average)/2
    if average2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", "%.1f" % average2)
    elif average2 <= 4.9:
        print("Aluno reprovado.")
        print("Media final:", "%.1f" % average2)

