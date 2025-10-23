def remove(numbers):
    numbers.pop(0)
    return numbers
a = int(input("Enter a number to remove: "))
numbers = [1, 2, 3, 4, 5]
print(remove(numbers))