# Suppose the values of variables 'a' and 'b' are 6 and 8 respectively,
# write two programs to swap the values of the two variables.
# 1 - first program by using a third variable
# 2 - second program without using any third variable
# (Swapping means interchanging the values of the two variables
# E.g.- If entered value of x is 5 and y is 10 then
# after swapping the value of x and y should become 10 and 5 respectively.)



s_ab = input("Enter 2 values a, b separated by space: ")
a, b = map(int, s_ab.split())

print("a=", a, "b=", b)

# Swap using 3 variables
c = a
a = b
b = c

print("SWAP 3 VAR:", "a=", a, "b=", b)

# Swap using 2 variable
a = a + b

b = a - b
a = a - b
print("SWAP again NO VAR", "a=", a, "b=", b)

# Alternative using function
def swap1(x, y):
    yield y
    yield x
a, b = swap1(a, b)
print("SWAP again yield", "a=", a, "b=", b)

