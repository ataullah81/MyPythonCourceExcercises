import datetime as dt

birth_day = input("Enter the date of your birth (dd-mm-yyyy): ")
today = dt.datetime.today()
birth_date = dt.datetime.strptime(birth_day, "%d-%m-%Y")

if today.day == birth_date.day and today.month == birth_date.month:
    print("Today is your birthday!")
else:
    print("Today is not your birthday!")