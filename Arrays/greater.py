num=[1,2,3,4,5]

def greater(num):  
    g=num[0] 
    for i in range (len(num)):
        if g<num[i]:
            g=num[i]
    print(f"geatest is {g}")

def least(num):
    le=num[0]
    for i in range (len(num)):
        if le>num[i]:
            le=num[i]
    print(f"least is {le}")
greater(num)
least(num)