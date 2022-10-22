prod_code1, prod_unit1, unit_price1 = input().split()
prod_code_1 = int(prod_code1)
prod_unit_1 = int(prod_unit1)
unit_price_1 = float(unit_price1)

prod_code2, prod_unit2, unit_price2 = input().split()
prod_code_2 = int(prod_code2)
prod_unit_2 = int(prod_unit2)
unit_price_2 = float(unit_price2)

total = prod_unit_1 * unit_price_1 + prod_unit_2 * unit_price_2

print("VALOR A PAGAR: R$ ""%.2f" % total)