def occ(a):
    result = []           # create an empty list to store unique elements
    for i in a:           # go through each number in original list
        if i not in result:  # check if it is already in result list
            result.append(i) # if not, add it
    return result         # finally return only unique elements

a = [1,2,3,4,2,5,1,2,3,4,2]
print(occ(a))
