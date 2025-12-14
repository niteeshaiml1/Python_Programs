nums = eval(input("Enter a list of numbers (e.g., [2,4,3,6,7,9]): "))
k = int(input("Enter number of rotations: "))

k = k % len(nums)                # handle overflow
rotated = nums[-k:] + nums[:k]  # manual rotation

print(rotated)
