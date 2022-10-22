note = float(input())
print("NOTAS:")
note100 = note / 100
note100_remainder = note % 100
print("%d" % note100, "nota(s) de R$ 100.00")
note50 = note100_remainder / 50
note50_remainder = note100_remainder % 50
print("%d" % note50, "nota(s) de R$ 50.00")
note20 = note50_remainder / 20
note20_remainder = note50_remainder % 20
print("%d" % note20, "nota(s) de R$ 20.00")
note10 = note20_remainder / 10
note10_remainder = note20_remainder % 10
print("%d" % note10, "nota(s) de R$ 10.00")
note5 = note10_remainder / 5
note5_remainder = note10_remainder % 5
print("%d" % note5, "nota(s) de R$ 5.00")
note2 = note5_remainder / 2
note2_remainder = note5_remainder % 2
print("%d" % note2, "nota(s) de R$ 2.00")
coin = note2_remainder * 100
print("MOEDAS:")
coin1 = coin / 100
coin1_remainder = coin % 100
print("%d" % coin1, "moeda(s) de R$ 1.00")
coin50 = coin1_remainder / 50
coin50_remainder = coin1_remainder % 50
print("%d" % coin50, "moeda(s) de R$ 0.50")
coin25 = coin50_remainder / 25
coin25_remainder = coin50_remainder % 25
print("%d" % coin25, "moeda(s) de R$ 0.25")
coin10 = coin25_remainder / 10
coin10_remainder = coin25_remainder % 10
print("%d" % coin10, "moeda(s) de R$ 0.10")
coin5 = coin10_remainder / 5
coin5_remainder = coin10_remainder % 5
print("%d" % coin5, "moeda(s) de R$ 0.05")
coin1 = coin5_remainder / 1
coin1_remainder = coin5_remainder % 1
print("%d" % coin1, "moeda(s) de R$ 0.01")


