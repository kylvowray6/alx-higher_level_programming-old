#!/usr/bin/python3

# Loop through digits 0-8 for the first digit
for i in range(9):
    # Loop through digits i+1 to 9 for the second digit
    for j in range(i + 1, 10):
        if i != j:  # Ensure the digits are different
            if i == 8 and j == 9:  # Last combination
                print("{}{}".format(i, j))
            else:
                print("{}{}, ".format(i, j), end='')

