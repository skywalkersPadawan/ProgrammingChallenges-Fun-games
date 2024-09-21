"""
ChallengeTitle: Power Calculator
Create a function that takes voltage and current and returns the calculated power.

Examples
circuit_power(230, 10) ➞ 2300

circuit_power(110, 3) ➞ 330

circuit_power(480, 20) ➞ 9600
Notes
Requires basic calculation of electrical circuits (see Resources for info).
"""


def circuit_power(voltage, current):
    return voltage * current


# test cases for the function
assert circuit_power(110, 3) == 330, "Power for 110V and 3A should be 330W."
assert circuit_power(230, 10) == 2300, "Power for 230V and 10A should be 2300W."
assert circuit_power(480, 20) == 9600, "Power for 480V and 20A should be 9600W."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
