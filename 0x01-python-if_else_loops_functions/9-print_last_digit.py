#!/usr/bin/python3
def last_digit(number):
    last_d = (number % 10) if number >= 0 else ((number * -1) % 10)
    print("{:d}".format(lastd), end='')
    return(last_d)
