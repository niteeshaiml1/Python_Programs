text = input("Enter a string: ")

letters = digits = specials = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        specials += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Characters:", specials)
