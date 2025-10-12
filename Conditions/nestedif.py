tempearture=int(input("Enter temperature: "))
if tempearture<0:
    print("Freezing weather")
elif tempearture>=0 and tempearture<=20:
    print("Cold weather")
elif tempearture>30:
    print("Hot weather")