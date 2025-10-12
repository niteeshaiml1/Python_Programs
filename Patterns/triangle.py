a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
if a==b and b==c:
    print("equilateral triangle")
elif a==b!=c or b==c!=a or a==c!=b:
    print("isosceles triangle")
else:
    print("scalene triangle")    