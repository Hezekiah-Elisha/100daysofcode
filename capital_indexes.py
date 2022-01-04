def capital_indexes(strng):
    lst = []
    for index, value in enumerate(strng):
        if value >= "A" and value <= "Z":
            lst.append(index)
    return lst