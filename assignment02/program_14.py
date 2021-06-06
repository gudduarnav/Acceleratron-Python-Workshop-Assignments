# 14. Ask user to enter age, sex (M or F ), marital status ( Y or N )
# and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then
# he will work in urban areas only. And any other input of age should print "ERROR".

age = int(input("Enter Age:"))
sex = input("Enter Sex (M/F):").lower().strip()
maritalstatus = input("Enter Marital Status (Y/N):").lower().strip()

if "f" in sex:
    print("You will work only in urban areas")
elif "m" in sex and 24 <= age <= 40:
    print("You can work anywhere")
elif "m" in sex and 40 <= age <= 60:
    print("You can work in urban areas only")
else:
    print("ERROR")