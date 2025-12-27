def seq_lett(s):
    for i in range(len(s)-1):
        if ord(s[i]) + 1 == ord(s[i+1]):
            return True
    return False
s=input("Enter a string: ")
print(seq_lett(s))