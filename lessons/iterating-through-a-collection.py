"""Example of looping through all characters in a string."""

user_string: str = input("Give me a string! ")

# The variable I is a common counter variable name in programming. I is short for iteration.
i: int = 0
while i < len(user_string):
    print(user_string[i])
    i = i + 1  

print("Done!")