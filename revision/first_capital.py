def first_capital(text):
    for ch in text:
        if ch.isupper():
            return ch
text=input("Enter a string: ")
print(first_capital(text))