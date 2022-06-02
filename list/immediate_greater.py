def immediate_greater(arr, x):
    new_arr = [y for y in arr if y > x]
    
    return min(new_arr) if arr else -1

print(immediate_greater([10, 20, 30, 40, 50], 30))