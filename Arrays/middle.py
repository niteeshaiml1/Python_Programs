def func(numbers):
    if len(numbers)%2==0:
        return numbers[(len(numbers)//2)-1] , numbers[int(len(numbers))//2]
    else:
        return numbers[int(len(numbers))//2]
numbers = [1, 2, 3, 4, 5,6,7]
print(func(numbers))