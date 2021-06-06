# 18. Write a program to find the sum of the even and
# odd digits of the number which is given as input.
# (e.g 5624 evenPlaceSum=5+2=7 oddPlaceSum = 6+4=10)

number = int(input("Enter a number:"))

print("Number is", number)

digit_array = list(map(int, list(str(number))))
print("Digits are", digit_array)

even_digit = digit_array[0::2]
odd_digit = digit_array[1::2]

print("Even Place Digits are", even_digit)
print("Odd Place Digits are", odd_digit)

print("Even place sum=", sum(even_digit))
print("Odd place sum=", sum(odd_digit))