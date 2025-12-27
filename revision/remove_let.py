def remove(s,ip):
    for ch in s:
        if ch==ip:
            s=s.replace(ch,"")
    return s
s=input("Enter a string: ")
ip=input("Enter a character to remove: ")
print(remove(s,ip))