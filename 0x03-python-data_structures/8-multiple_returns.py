#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])


# Test the function with your example
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
