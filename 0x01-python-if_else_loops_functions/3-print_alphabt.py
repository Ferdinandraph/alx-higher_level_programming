#!/usr/bin/python3
for character in range(97, 122):
    if character == ord('e') or character == ord('q'):
        continue
    print("{:c}".format(character), end='')
