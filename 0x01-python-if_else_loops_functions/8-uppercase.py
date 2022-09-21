#!/usr/bin/python3
def to_uperchar(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def to_string(string):
    new_string = ''
    for x in string:
        new_string += "%c" % to_uperchar(x)
    print("{:s}".format(new_string))
