"""
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
"""

prev = 0
for num in range(11):
    sum = prev + num
    print(f'Current number: {num}. Previous number: {prev}. Sum: {sum}')
    prev  = num
