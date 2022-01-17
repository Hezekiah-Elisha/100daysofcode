#!/usr/bin/python3

# A python program that returns the count of strings separated by a hyphen delimiter
def count(strg):
    lst = strg.split("-")
    return len(lst)