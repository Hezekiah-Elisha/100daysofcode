#!/usr/bin/python3

def add_dot(str1):
    list1 = list(str1)
    for i in range(len(str1) - 1):
        list1[i] = list1[i] + "."
    value = "".join(list1)
    return value

def remove_dot(str1):
    return str1.replace(".", "")