# 10. If
# x = 2
# y = 5
# z = 0
# then find values of the following expressions:
# a. x == 2
# b. x != 5
# c. x != 5 && y >= 5
# d. z != 0 || x == 2
# e. !(y < 10)

x = 2
y = 5
z = 0

print("x==2 is", (x==2))

print("x!=5 is", (x!=5))

#print("x!=5 && y>=5", (x!=5 && y>=5))  <- Invalid replace && by and
print("x!=5 and y>=5", (x!=5 and y>=5))

#print("z!=0 || X==2", (z!=0 || x==2))  <- Invalid replace || by or
print("z!=0 or X==2", (z!=0 or x==2))

#print("!(y<10)", !(y<10))  <- Invalid replace ! by not
print("not(y<10)", not (y<10))
