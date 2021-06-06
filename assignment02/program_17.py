# 17. Take 10 integers from keyboard using loop and print their average value on the screen. (use array to store inputs).

numbers = list(map(int, input("Enter 10 numbers:").split()))

if len(numbers) >= 10:
    numbers = numbers[0:10]
    print("10 Numbers are", numbers)
    print("Average=", sum(numbers)/len(numbers))

