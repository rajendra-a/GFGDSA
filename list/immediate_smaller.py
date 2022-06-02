def immediate_smaller(arr,x):
    ism = -1
    for i in arr:
        if i < x and i > ism:
            ism = i
    return ism
print(immediate_smaller( [10, 20, 30, 40, 50], 30))

def ism(arr, x):
    new_arr = [y for y in arr if y < x]
    return max(new_arr) if new_arr else -1

print( ism( [10, 20, 30, 40, 50], 30))