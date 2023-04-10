"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
import datetime

age = int(input('How old are you?'))

year = datetime.date.today().year
year_birth = year - age
year_100 = year_birth + 100

print(f"If you have {age} years, you born in {year_birth} and in {year_100} you'll have 100 years")

