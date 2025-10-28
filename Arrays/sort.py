def sort(a):
    n = len(a)
    # Repeat passes to move largest numbers to the end
    for _ in range(n):
        # Compare each element with the next
        for i in range(n-1):
            if a[i] > a[i+1]:
                # Swap if current is greater than next
                a[i], a[i+1] = a[i+1], a[i]
    return a

a = [5, 3, 1, 4, 2]
print(sort(a))
