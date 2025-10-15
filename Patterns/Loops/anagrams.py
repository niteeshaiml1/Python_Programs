a = input("enter string1:")
b = input("enter string2:")

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] not in b:
            print("not anagram")
            break
    else:
        print("anagram")
else:
    print("not anagram")
