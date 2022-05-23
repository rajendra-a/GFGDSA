def get_smaller(lst, num):
    result = []
    for x in lst:
        if x < num:
            result.append(x)
    return result
        
print(get_smaller([3, 4, 5, 454, 5454, 54543, 5, 87, 88], 7))
