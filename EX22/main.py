def is_leap_year(A):
    if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")