#!/usr/bin/python3

def uppercase(input_str):
    output_str = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        output_str += uppercase_char

    count_print = 0
    for char in output_str:
        if count_print < 2:
            print("{}".format(char), end='')
            count_print += 1
        else:
            print("{}".format(char))
            count_print = 0

    if count_print != 0:
        print()

# Test cases
if __name__ == "__main__":
    uppercase("holberton")
    uppercase("Holberton School")
    uppercase("Holberton School, 98 battery street")
    uppercase("")
    uppercase(98)
    uppercase("z")
