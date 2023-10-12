#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())


    # Iterate through the sorted keys and print each key-value pair
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))


# Example usage:
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
