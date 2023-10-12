#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_sum = 0  # Initialize a variable to store the sum of unique integers


    # Use a set to keep track of unique integers
    unique_set = set()


    for num in my_list:
        # Check if the number is not in the set (i.e., it's unique)
        if num not in unique_set:
            unique_set.add(num)  # Add the unique number to the set
            unique_sum += num  # Add the unique number to the sum


    return unique_sum

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
