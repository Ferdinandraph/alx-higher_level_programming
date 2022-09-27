#!/usr/bin/python3
def max_integer(my_list=[]):
    max_No = 0
    for i in my_list:
        if i > max_No:
            max_No = i
    return(max_No)
