#!/usr/bin/python3
"""
Prints the ASCII alphabet in lowercase, not followed by a new line.
"""

# Use a list comprehension to generate the characters
alphabet = [chr(c) for c in range(97, 123)]

# Use a single print function with string formatting to join the characters
print("".join(alphabet), end="")

