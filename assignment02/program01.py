# check rectangle or square

length, breadth = map(float, input("Enter length and breadth (separated by comma):").split(","))
epsilon = 0.00001

if abs(length - breadth) < epsilon:
    print("Entered dimension represents a Square")
else:
    print("Entered dimension represents a Rectangle")


