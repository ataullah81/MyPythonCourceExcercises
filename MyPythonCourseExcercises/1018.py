bankNote = int(input())

print(bankNote)

bankNote100 = bankNote/100
bankNote100_remainder = bankNote % 100
print("%d" % bankNote100, "nota(s) de R$ 100,00")
bankNote50 = bankNote100_remainder / 50
bankNote50_remainder = bankNote100_remainder % 50
print("%d" % bankNote50, "nota(s) de R$ 50,00")
bankNote20 = bankNote50_remainder / 20
bankNote20_remainder = bankNote50_remainder % 20
print("%d" % bankNote20, "nota(s) de R$ 20,00")
bankNote10 = bankNote20_remainder / 10
bankNote10_remainder = bankNote20_remainder % 10
print("%d" % bankNote10, "nota(s) de R$ 10,00")
bankNote5 = bankNote10_remainder / 5
bankNote5_remainder = bankNote10_remainder % 5
print("%d" % bankNote5, "nota(s) de R$ 5,00")
bankNote2 = bankNote5_remainder / 2
bankNote2_remainder = bankNote5_remainder % 2
print("%d" % bankNote2, "nota(s) de R$ 2,00")
bankNote1 = bankNote2_remainder / 1
bankNote1_remainder = bankNote2_remainder % 1
print("%d" % bankNote1, "nota(s) de R$ 1,00")


