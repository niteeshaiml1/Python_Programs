example="niteesh issssssssssssssssssss a good boy"
words=example.split(" ")
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print("The longest word is:",longest)
