marks=int(input("enter your marks:"))
if marks>=21:
    if marks>=91:
        print("grade A")
    elif marks>=81:
        print("grade B")
    elif marks>=71:
        print("grade C")        
    else:
        print("grade D")    
else:
    print("fail")        