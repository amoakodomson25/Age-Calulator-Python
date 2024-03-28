import datetime 

day = int(input("Day of birth: "))
month = int(input("Month of birth: "))
year = int(input("Year of birth: "))
DOB = datetime.date(year,month,day)
today = datetime.date.today()



years = today.year - DOB.year - ((today.month,today.day)<(DOB.month,DOB.day))
months = abs(today.month - DOB.month)
days =abs(today.day - DOB.day)
print()
print(f"You are {years}years, {months}months and {days}days old.")
print()