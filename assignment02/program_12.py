# 12. Print ASCII values and their equivalent characters. ASCII value vary from 0 to 255.

ch = input("Enter a Character:")
if len(ch)>=1:
    ch = ch[0]

    # way 1
    chasc = ord(ch)
    print("ASCII of", ch,"is", chasc)

    # way 2
    chasc = ch.encode("UTF-8")
    print("ASCII of", ch,"is", int(chasc[0]))