def string_palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False
text=input("Enter a string: ")
print(string_palindrome(text))