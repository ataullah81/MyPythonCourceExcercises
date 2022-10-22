ageInDays = int(input())
years = ageInDays/365
remainderYears = ageInDays % 365
days = remainderYears/30
month = remainderYears % 30

print("%d" % years, "ano(s)")
print("%d" % days, "mes(es)")
print("%d" % month, "dia(s)")
