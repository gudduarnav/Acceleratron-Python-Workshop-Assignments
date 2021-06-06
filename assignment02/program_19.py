# 19. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers

a, b = map(int, input("Enter 2 numbers:").split())

print("Numbers are",a,b)


# find gcd
gcd = a
div = b

while True:
    remainder = div % gcd
    if remainder == 0:
        # gcd found
        break
    else:
        # swap
        div = gcd
        gcd = remainder


print("GCD is", gcd)

# find lcm
print("LCM is", (a*b)//gcd)