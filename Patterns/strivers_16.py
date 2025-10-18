n=5
c=64
for i in range (n):
    c+=1
    for j in range (i+1):
        print(chr(c),end=" ")
        
    print()
# A 
# B B 
# C C C
# D D D D
# E E E E E