a=int(input("Enter coefficient of x^2: "))
b=int(input("Enter coefficient of x: "))
c=int(input("Enter constant term: "))
x1=(-b+(b**2-4*a*c)**1/2)/2*a
x2=(-b-(b**2-4*a*c)**1/2)/2*a
print("Roots are: ",x1,x2)
