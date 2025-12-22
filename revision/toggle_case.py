def toggle_case(text):
    result = ""
    for ch in text:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

text = input("Enter a string: ")
print(toggle_case(text))
