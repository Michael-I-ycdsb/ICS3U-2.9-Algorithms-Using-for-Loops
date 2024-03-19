"""
File: factorial.py
Author: Michael Iacobelli
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             factorial n! outputting the final value.
"""

# defines variables
input_num = int(input("Enter a number: "))
factorial_value = (input_num)

# loops for every int in range of input_num exept last
for num in range(1, input_num):
    # multiplies factorial_value by num in range
    factorial_value *= num

print(f'{input_num}! = {factorial_value}')