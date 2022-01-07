def capital_indexes(strg):
    lst = []
    for index, value in enumerate(strg):
        if value >= "A" and value <= "Z":
            lst.append(index)
    return lst
