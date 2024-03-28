import datetime 
try:
    print()
    day = int(input("Enter day of birth: "))
    month = int(input("Enter month of birth: "))
    year = int(input("Enter year of birth: "))
    DOB = datetime.date(year,month,day)
    today = datetime.date.today()
    years = today.year - DOB.year - ((today.month,today.day)<(DOB.month,DOB.day))
    months = abs(today.month - DOB.month)
    days =abs(today.day - DOB.day)
    print()
    print(f"You are {years}years, {months}months and {days}days old.")
    print()
except ValueError:
    print()
    print("Invalid input, Please enter a valid integer")
    print()
