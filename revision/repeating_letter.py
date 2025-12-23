def repeat(s):
    max=0
    for ch in s:
        x=s.count(ch)
        if x>max:
            max=x
            char=ch
    return max,char

s=input("Enter a string: ")
print(repeat(s))