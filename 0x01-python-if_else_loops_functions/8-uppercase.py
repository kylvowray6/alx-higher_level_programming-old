#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end='')

    print()  # Print a new line at the end

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
