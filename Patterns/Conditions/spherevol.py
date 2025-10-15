pi=3.14
r=float(input("Enter radius of sphere: "))
if r>=0:
    vol=4/3*pi*r**3
    print("volume:",vol)
else:
     print("Radius cannot be negative")
