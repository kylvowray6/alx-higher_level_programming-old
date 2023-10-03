#!/usr/bin/python3

# Print numbers from 0 to 99 separated by ', ' and with two digits
for num in range(100):
    if num < 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))

