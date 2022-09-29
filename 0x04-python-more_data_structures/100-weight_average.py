#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return(0)
    avrgScore = 0
    size = 0
    for tuple in my_list:
        avrgScore += (tuple[0] * tuple[1])
        size += tuple[1]
    return(avrgScore/size)
