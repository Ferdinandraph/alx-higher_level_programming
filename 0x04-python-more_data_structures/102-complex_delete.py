#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """program that deletes keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        # destructing
        for i, j in a_dictionary.items():
            if j == value:
                del a_dictionary[i]
                break
    return (a_dictionary)
