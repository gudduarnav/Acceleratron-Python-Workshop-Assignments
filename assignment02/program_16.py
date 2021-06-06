# 16. Take integer inputs from user until he/she presses q
# ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.

allnumbers = list()
while True:
    user = input("Enter a number (q to Quit):")
    if "q" in user.lower():
        break
    else:
        allnumbers.append(int(user))


total = 0
count = 0
product = 1

for onenumber in allnumbers:
    count += 1
    total += onenumber
    product *= onenumber

average = 0
if count > 0:
    average = total / count

print("Average = ", average)
print("Product = ", product)