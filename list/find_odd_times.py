def odd_times_number(l):
    result = None
    for x in l:
        count = l.count(x)
        if count%2 != 0:
            result = x
            break
    return result

print(odd_times_number([10, 20, 20, 10, 30]))