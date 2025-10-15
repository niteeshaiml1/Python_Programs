pin=input("enter your pin:")
balance=20000
if pin=="1234":
    amount=int(input("enter amount to withdraw:"))
    if amount>balance:
        print("insufficient balance")
    else:
        balance-=amount
        print(f"withdrawal successful. remaining balance is {balance}")   
else:    
    print("incorrect pin")