def mid(strg):
    if len(strg) % 2 == 0:
        return ""
    else:
        index = len(strg) // 2
        return strg[index]
