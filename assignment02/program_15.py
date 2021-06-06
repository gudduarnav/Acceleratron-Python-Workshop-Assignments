# 15. A 4-digit number is entered through keyboard.
# Write a program to print a new number with digits reversed as of original one. E.g.-
# INPUT: 1234 OUTPUT: 4321
# INPUT: 5982 OUTPUT: 2895

num_in : int = abs(int(input("Enter a number: ")))

# Way 1
num : int = num_in
rnum : int= 0

while num>0:
    rnum *= 10
    rnum += num % 10
    num //= 10

print("input=", num_in, "output=", rnum)

# Way 2
num = str(num_in)
rnum = num[: : -1]
rnum = int(rnum)

print("input=", num_in, "output=", rnum)
