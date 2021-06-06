# Take the marks of a student obtained in 5 subjects (each out of 100),
# write a program to calculate total marks and percentage marks.

s_marks = input("Enter marks in 5 subjects separated by comma (,):")
marks = list(map(float, s_marks.split(",")))

total_marks = sum(marks)
subject_count = len(marks)
ave_marks = total_marks / subject_count

print("Marks in", subject_count,"subjects are", marks)
print("Total Marks in", subject_count,"subjects = ", total_marks)
print("Average Marks in", subject_count,"subjects = ", ave_marks)