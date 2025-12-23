def even(s):
    x=s.split()
    result=[]
    for ch in x:
        if len(ch)%2==0:
            result.append(ch)
    return result    
    
s=input("Enter a string: ")
print(even(s))