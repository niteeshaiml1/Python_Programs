def occurance(digit):
    count=0
    for i in str(num):
        if i==str(digit):
            count+=1
    return count

num=int(input("Enter a number: "))
digit=int(input("Enter a digit to find its occurance: "))
print(occurance(digit))