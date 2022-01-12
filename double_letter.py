#!/usr/bin/python3

def double_letter(strg):
    for index in range(len(strg) - 1):
        if strg[index] == strg[index + 1]:
            return True
    return False