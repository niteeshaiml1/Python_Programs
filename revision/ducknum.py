def ducknum(num):
    if str(num)[0]=="0":
        return False
    
    for ch in str(num):
        if ch=="0":
            return True
        
    return False
        
num=int(input("Enter a number: "))
print(ducknum(num))