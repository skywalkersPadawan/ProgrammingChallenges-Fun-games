"""
ChallengeTitle: Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
"""


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2


# test cases for the function
assert calculator(2, "/", 2) == 1
assert calculator(10, "-", 7) == 3
assert calculator(2, "*", 16) == 32
assert calculator(2, "-", 2) == 0
assert calculator(15, "+", 26) == 41
assert calculator(2, "+", 2) == 4
assert calculator(2, "/", 0) == "Can't divide by 0!"


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
