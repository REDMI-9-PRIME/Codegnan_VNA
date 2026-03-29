para= input("Enter a paragraph:")
vowels = 0
#vowels include "aeiou"
consonants = 0
para = para.lower()

for ch in para:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("In this paragraph, the vowels count is",vowels)
print("In this paragraph, the consonants count is",consonants)
    
