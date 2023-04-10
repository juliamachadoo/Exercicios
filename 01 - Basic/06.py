"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

"""

number = int(input('Type a number: '))
if number % 4 == 0 and number % 2 == 0:
    print(f'Number {number} is even and multiple of 4')
elif number % 2 == 1:
    print(f'Number {number} is odd')
elif number % 4 == 0:
    print(f'Number {number} is even')