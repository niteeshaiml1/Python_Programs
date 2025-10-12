num = 12233344
d = int(input("Enter a digit to find its occurrence: "))
count = 0
n = num  # Use a copy of num to preserve original number

while n > 0:              # Corrected: use 'while', not 'for'
    r = n % 10            # Get last digit
    if r == d:
        count += 1
    n = n // 10           # Remove last digit
print(f"The digit {d} occurs {count} times in {num}")

