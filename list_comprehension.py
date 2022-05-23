# Even list python code
even_list = []
for x in range(11):
    if x%2 == 0:
        even_list.append(x)
print(even_list)


# Similar even list comprehension
even_lst = [x for x in range(11) if x%2 == 0]
print(even_lst)


# Odd list python code
odd_list = []
for y in range(11):
    if y%2 != 0:
        odd_list.append(y)
print(odd_list)


# Similar odd list  comprehension
odd_list = [y for y in range(11) if y%2 != 0]
print(odd_list)



# List comprehension function to return smaller numbers than given number
def get_smaller(l, y):
    return [x for x in l if  y < x]

# List comprehension to get even and odd numbers lists
def even_odd(l):
    even = [x for x in l if x%2 == 0]
    odd = [y for y in l if y%2 != 0]
    return even, odd

# Some list comprehension problems 
string = "geeksforgeeks"

list5 = [x for x in string if x in "aeiou"]
print(list5)