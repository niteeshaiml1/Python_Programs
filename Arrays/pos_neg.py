def count_pos_neg(numbers):
    positive = 0
    negative = 0
    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        # zeros are ignored here
    print(f"Positive count: {positive}, Negative count: {negative}")

num = [1, 2, 3, 4, 5, 6, -7, -8, -8]
count_pos_neg(num)
