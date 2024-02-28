#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for element in my_string:
        if element != 'c' and element != 'C':
            result += element
    return result
