# Function to check birthday
def check_date(ip_month, ip_day):
    month = "november"
    day = 4
    if ip_month.lower() == month and ip_day == day:
        return 1
    else:
        return 0

# Input from user
ip_month = input("Enter month: ")
ip_day = int(input("Enter day: "))

# Call the function
result = check_date(ip_month, ip_day)

# Print the result (1 if birthday, 0 otherwise)
print(result)
