# Write a program to convert Fahrenheit into Celsius. Take Fahrenheit as input.

fah = float(input("Enter Temperature in Fahrenheit:"))

cel = (fah - 32) * 5 / 9

print(round(fah, 2) ,"\u00B0F =", round(cel, 2), "\u00B0C")