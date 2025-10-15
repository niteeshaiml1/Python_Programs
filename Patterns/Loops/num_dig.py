a=int(input("enter a number:"))
if a>9:
    print("number has more than one digit")
    if a/10<=9:
        print("number has two digits")
    elif a//100<=9:
        print("number has three digits")
