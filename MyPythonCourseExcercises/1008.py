employee_n = int(input())
work_hour = int(input())
salary_p_h = float(input())

salary = (work_hour*salary_p_h)
print("NUMBER =", employee_n)
print("SALARY = U$ {}".format("%.2f" % salary))

"""
25
100
5.50
NUMBER = 25
SALARY = U$ 550.00
"""