num=int(input("Enter a number: "))
#i=1
fact=1
#while i<=num:
 #   fact=fact*i
  #  i+=1
    
#print(f"factorial of {num} is {fact}")    
for i in range(1,num+1):
    fact=fact*i
print(f"factorial of {num} is {fact}")