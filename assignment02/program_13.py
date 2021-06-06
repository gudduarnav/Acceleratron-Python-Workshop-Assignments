# 13. Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year
# but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter Year:"))
mod_4 = year % 4
mod_400 = year % 400
mod_100 = year % 100

if mod_100 == 0:
    if mod_400 == 0:
        print(year,"is a leap year (century)")
    else:
        print(year,"is not a leap year (century)")
else:
    if mod_4 == 0:
        print(year,"is a leap year")
    else:
        print(year, "is not a leap year")