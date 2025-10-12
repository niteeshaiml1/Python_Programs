password = input("Enter your password: ")

# Check each condition directly
length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

# Final verdict using conditions only
if length_ok and has_upper and has_lower and has_digit and has_symbol:
    print("Password Strength: STRONG ✅")
else:
    print("Password Strength: WEAK ❌")
