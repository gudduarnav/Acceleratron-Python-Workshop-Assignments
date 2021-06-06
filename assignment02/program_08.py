# 8. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended is student is allowed to sit in exam or not.

total_classes = int(input("Enter Number of classes held:"))
attendance = int(input("Enter Number of classes attended:"))
percent = attendance * 100.0 / total_classes
min_percent = 75.0

if percent >= min_percent:
    print("You have attendance of", round(percent,2)," % and You are ALLOWED for Exam")
else:
    print("You have attendance of", round(percent,2)," % and You are NOT ALLOWED for Exam")