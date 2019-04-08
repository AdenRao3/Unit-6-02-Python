# Created by: Aden Rao
# Created on: April 7, 2019
# This program lets a user enter a number and it tells them if the number is positive or negative.

# Function for importing math
import math

# Input that lets teh user enter a number and tells them to enter a number
integer = int(input("Type a number: "))

# If statement for determining if the number is negative or postitive
if integer > 0:
	print("Positive integer")
	print()
elif integer < 0:
	print("Negative integer")
	print()
else:
	print("Neutral or 0")
