#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_No = 0
    for i in range(len(my_list)):
        if my_list[i] > max_No:
            max_No = my_list[i]
    return(max_No)
print(max_integer([2, 4, 66, 68]))
