def next_letter(s):
    result=""
    for ch in s:
        result+=chr(ord(ch)+1)
    return result
   
s=input("Enter a string: ")
print(next_letter(s))