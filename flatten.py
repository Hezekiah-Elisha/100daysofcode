#!/usr/bin/python3

def flatten(list1):
    result = []
    for element in list1:
        for value in element:
            result.append(value)
    return value