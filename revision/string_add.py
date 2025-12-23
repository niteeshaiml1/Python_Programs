def string(s1,s2):
    return s1[0].upper()+s1[1:].lower() + s2
s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(string(s1,s2))