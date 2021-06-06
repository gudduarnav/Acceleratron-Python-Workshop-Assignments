# 6. Take input of age of 3 people by user and determine oldest and youngest among them.

ages = list(map(int, input("Enter age of 3 people: ").split()))
print("Minimum age is", min(ages))