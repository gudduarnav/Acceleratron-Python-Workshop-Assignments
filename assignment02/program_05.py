# 5. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = float(input("Enter Marks (from 0 to 100):"))

classes =[
    {"grade": "F", "marks": (0, 25)},
    {"grade": "E", "marks": (25, 45)},
    {"grade": "D", "marks": (45, 50)},
    {"grade": "C", "marks": (50, 60)},
    {"grade": "B", "marks": (60, 80)},
    {"grade": "A", "marks": (80, 100)},
]

for classes1 in classes:
    if classes1["marks"][0] <= marks < classes1["marks"][1]:
        print("You obtained Grade", classes1["grade"])
        break

