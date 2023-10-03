#!/usr/bin/python3

def uppercase(input_str):
    output_str = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        output_str += uppercase_char

    print(output_str)

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
