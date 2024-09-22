"""
ChallengeTitle: Luke, I Am Your ...
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
Notes
N/A
"""


def relation_to_luke(name):
    person = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
    }

    return f"Luke, I am your {person[name]}."


# test cases for the function
assert relation_to_luke("Darth Vader") == "Luke, I am your father."
assert relation_to_luke("Leia") == "Luke, I am your sister."
assert relation_to_luke("Han") == "Luke, I am your brother in law."
assert relation_to_luke("R2D2") == "Luke, I am your droid."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
