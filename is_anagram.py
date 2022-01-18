#!/usr/bin/python3

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# SIMILAR WAY TO SOLVE THE ABOVE CODE
def is_anagram(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()

    matches = True
    index = 0

    while index < len(str1) and True:
        if list1[index] == list2[index]:
            index += 1
        else:
            matches = False
    return matches