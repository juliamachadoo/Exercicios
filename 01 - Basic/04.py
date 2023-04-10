"""
Write a program to remove characters from a string starting from zero up to n and return a new string.
"""

word = input('Enter a word: ')
num_char = int(input('How many characters do you want to remove? '))
location = input('Do you want to remove from Beggining or ftom the End? [B] Beggining [E] End ')

size = len(word)

if location == 'B' or 'b':
    new_word = word[num_char:]
    print(new_word)
else:
    new_word = word[:-num_char]
    print(new_word)