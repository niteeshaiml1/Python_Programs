def freq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq, max(freq,key=freq.get)
s=input("Enter a string: ")
print(freq(s))