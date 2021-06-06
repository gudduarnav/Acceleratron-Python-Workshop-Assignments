# 11. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

ch = input("Enter a Character:")
if len(ch) >= 1:
    ch = ch[0]

    if ch.isupper():
        print(ch,"is UPPER CASE")
    elif ch.islower():
        print(ch,"is LOWER CASE")
    else:
        print(ch, "I do not know!!!")