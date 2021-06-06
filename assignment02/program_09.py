# 9. Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

total_classes = int(input("Enter Number of classes held:"))
attendance = int(input("Enter Number of classes attended:"))
percent = attendance * 100.0 / total_classes
min_percent = 75.0

if percent >= min_percent:
    print("You have attendance of", round(percent,2)," % and You are ALLOWED for Exam")
else:
    medical_choice = input("Do you have a medical cause (Y/N)?")
    if "y" in medical_choice.lower():
        print("You have attendance of", round(percent, 2), " % and You are ALLOWED for Exam because of MEDICAL PROBLEM")
    else:
        print("You have attendance of", round(percent,2)," % and You are NOT ALLOWED for Exam")
