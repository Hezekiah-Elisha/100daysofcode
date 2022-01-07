#!/usr/bin/python3
def online_count(statuses):
    count = 0
    for key, value in statuses.items():
        if value == 'online':
            count += 1
    return(count)
