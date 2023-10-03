#!/usr/bin/python3

def pow(a, b):
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    for _ in range(b):
        result *= a

    return round(result, 2)  # Round to 2 decimal places

# Test cases
if __name__ == "__main__":
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
    print(pow(10, -2))
    print(pow(-98, -10))
