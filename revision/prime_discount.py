def prime_discount(bill):
    temp = bill
    prime_sum = 0

    while temp > 0:
        dig = temp % 10
        temp //= 10

        if dig > 1:
            for i in range(2, dig):
                if dig % i == 0:
                    break
            else:
                prime_sum += dig   # prime digit

    return bill - prime_sum


bill = int(input("Enter bill amount: "))
print("Discounted bill amount is", prime_discount(bill))
