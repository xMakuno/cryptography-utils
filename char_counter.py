phrase = input("Enter the phrase to count its characters")
characters = 0
for c in phrase:
    banned_chars = " ,;.!:"
    if c not in banned_chars:
        characters+=1
print(f"The amount of chars in the phrase is: {characters}")