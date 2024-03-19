"""
File: sum.py
Author: Michael Iacobelli
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             sum of numbers from 1 to n using an accumulator variable.
"""

def sum_loop() -> None:
    # defines variables
    num_sum = 0
    input_num = int(input("Enter a number: "))

    # loops for every int in range of input_num
    for num in range(1, input_num + 1):
        # adds int to num_sum
        num_sum += num

    print(f'Sum of numbers from 1 to {input_num}: {num_sum}')


def sum_complex_O_1() -> None:
    # defines variables
    input_num = int(input("Enter a number: "))

    # calulates the sum of all numbers in range of input_num
    num_sum = int((input_num + 1) * (input_num / 2))

    print(f'Sum of numbers from 1 to {input_num}: {num_sum}')

sum_complex_O_1()