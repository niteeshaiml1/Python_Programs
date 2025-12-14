def cups(bought):
    total_cups=int(bought/6) + bought
    return total_cups
bought=int(input("Enter number of cups bought: "))
print(cups(bought))