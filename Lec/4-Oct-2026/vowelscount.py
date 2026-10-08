# Accept sentence and count the vowels

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels =", count)