# This module takes two numbers, adds them, and prints the result

import input_numbers

def add_numbers():
    num1, num2 = input_numbers.get_numbers()
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == '__main__':
    add_numbers()
