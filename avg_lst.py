# 
def avg_lst(l):
    sum = 0 
    for x in l:
        sum = sum + x
    n = len(l)
    return sum/n

print(avg_lst([1, 2, 3, 4]))

# without using library methods

def avg_lst(l):
    return sum(l)/len(l)

