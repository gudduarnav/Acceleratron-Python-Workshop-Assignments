# 4. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("Enter Salary: "))
years = float(input("Enter Years of Salary: "))

total_bonus = 0

if years > 5:
    bonus_per_year = salary * 5 / 100.0
    total_bonus = bonus_per_year * years

print("Total Bonus is", total_bonus)
