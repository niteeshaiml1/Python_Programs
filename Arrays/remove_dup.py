def remove_duplicates_inplace(lst):
    i = 0
    while i < len(lst):
        if lst[i] in lst[:i]:  # Check if element appeared before
            lst.pop(i)          # Remove duplicate
        else:
            i += 1
    return lst

num = [1, 2, 3, 2, 1, 4, 5, 4, 3]
num = remove_duplicates_inplace(num)
print(num)
