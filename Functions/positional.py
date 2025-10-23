def student(name, age, city):
    # Using the parameters to create a description
    return f"Name: {name}, Age: {age}, City: {city}"

# Calling using positional arguments
print(student("Niteesh", 19, "Hyd"))

# Calling using keyword arguments
print(student(age=19, city="Hyd", name="Niteesh"))
