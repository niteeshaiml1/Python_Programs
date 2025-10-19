n=4
for i in range (n):
    p=65 # ASCII for 'A'
    
    # 1. Print ascending part (A, AB, ABC, ABCD...)
    # Your logic for this loop was correct.
    # I only changed end=" " to end="" to match the image (e.g., "ABA" not "A B A").
    for j in range(i+1):
        print(chr(p),end="")
        p+=1
        
    # 2. Print descending part (B, CB, DCB...)
    
    # First, 'p' is now one *past* the peak (e.g., after 'ABC', p is 'D').
    # We must move it back two steps to get to the correct starting
    # character (e.g., 'B').
    p -= 2 
    
    # Second, this loop should run 'i' times.
    # (0 times for the first row, 1 time for the second, 2 for the third, etc.)
    for j in range(i):
        print(chr(p),end="")
        # Third, we need to *decrease* 'p' to go back down the alphabet.
        p -= 1
        
    # Go to the next line after the row is complete
    print()