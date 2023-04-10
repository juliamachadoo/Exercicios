"""
Write a program to accept a string from the user and display characters that are present at an even index number.
"""

word = input("Enter a word: ")
print(f'The word that you type was: {word}')

size = len(word)

print("Printing only even index chars")

for i in range(0, size - 1, 2):
    print(f"index[{i}]. Letter: {word[i]}")

