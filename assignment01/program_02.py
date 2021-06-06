# Given 3 sides of triangle
# Calculate Area of Triangle
# Heron's August

from math import sqrt

s_side = input("Enter the value of length of 3 sides (separated by space): ")
sideA, sideB, sideC = map(float, s_side.split())

print("Sides are", sideA, sideB, sideC)

# find perimeter of triangle
p = (sideA + sideB + sideC) / 2.0

# check if this is a triangle
if p>=sideA and p>=sideB and p>=sideC:
    # this is a good triangle
    # find area
    area = sqrt(p * (p - sideA) * (p - sideB) * (p - sideC))

    print("Area of Triangle = ", area)
else:
    # this is not a triangle
    print("ERROR: Not a valid triangle")
