def vow(s,n):
    vowels="aeiouAEIOU"
    count=0
    result=[]
    for ch in s:
        if ch in vowels:
            count+=1
            result.append(ch)
            if count==n:
                return result
s=input("Enter a string: ")
n=int(input("Enter number of vowels to find: "))
print(vow(s,n))