#a=int(input("Enter start point: "))
#b=int(input("Enter end point: "))
#for num in range (a,b+1):
 #   if num<2:
  #      continue
   # for i in range(2,num):
    #    if num % i == 0:
     #       is_prime=False
      #  else:
       #     is_prime=True
        #    if is_prime:
         #       print(num,end=", ")
a = int(input("Enter start point: "))
b = int(input("Enter end point: "))

for num in range(a, b + 1):
    if num < 2:
        continue  # skip numbers less than 2
    is_prime = True  # reset for each number
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # no need to check further
    if is_prime:
        print(num, end=", ")
