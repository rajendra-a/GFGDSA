# Largest element in the list
# Time complexity O(n)
def largest(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else: 
            return x
    return None


print(largest([10, 40, 30, 40, 50]))

# Largest element in the list 
# Time complexity
def largest_element(l):
    if not l: # checking if list is empty
        return None
    else:
        result = l[0]
        for i in range(1,len(l)):
            if l[i] > result:
                result = l[i]
    return result
print(largest_element([15, 6, 3, 3, 34]))


# Second largest element naive solution
def sec_largest_element(l):
    if len(l) <= 1:
        return None
    larg = largest_element(l)
    sec_lar = None
    for x in l:
        if x != larg:
            if sec_lar == None:
               sec_lar = x
            else:
               sec_lar = max(sec_lar, x)
    return sec_lar

# Efficient solution for second largest element
def get_sec_larg(l):
    if len(l) <= 1:
        return None

    larg = l[0]
    sec_larg = None

    for x in l[1:]:
        if x > larg:
            sec_larg = larg
            larg = x
        elif x != larg:
            if sec_larg == None or sec_larg < x:
                sec_larg = x
    return sec_larg

print(get_sec_larg([45, 65, 435, 45]))

