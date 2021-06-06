# compare number

firstNumber, secondNumber = map(int, input("Enter 2 numbers:").split())
greatest = firstNumber if firstNumber>secondNumber else secondNumber
print("Greatest Number is", greatest)

