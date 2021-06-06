# The total number of students in a class are 90 out of which 45 are boys.
# If 50% of the total students secured grade 'A' out of which 20 are boys,
# then write a program to calculate the total number of girls getting grade 'A'.

total_students = 90
boys = 45
total_gradeA = round(total_students * 50 / 100)
total_gradeA_boys = 20
total_gradeA_girls = round(total_gradeA - total_gradeA_boys)

print("Total Students = ", total_students)
print("Boys = ", boys)
print("Total Students scoring Grade A=", total_gradeA)
print("No. of Boys Scoring Grade A=", total_gradeA_boys)
print("No. of Girls Scoring Grade A=", total_gradeA_girls)


