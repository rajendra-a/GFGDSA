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

# Write a list comprehension that pri
string = "geeksforgeeks"
list5 = [x for x in string if x in "aeiou"]
print(list5)


# Write list comprehension that prints strings from the list which starts with letter g 
l2 = ['geeks', 'ide', 'courses', 'gfg']
l3 = [x for x in l2 if x.startswith('g')]
print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

# Dictionary comprehension that return key and value is cube of the key
l5 = [1, 2, 3, 4, 5]
d1 = {x:x**3 for x in l5}
print(d1)

# Write a dictionary comprehension that produces id  and its id number
d2 = {x:f"ID{x}" for x in range(5)} 
print(d2)

# # Write a dictionary comprehension that generated from two lists
l6 = [101, 102, 103]
l7 = ["gfg", "ide", "courses","tests"]
d3 = {l6[i]:l7[i] for i in range(len(l6))}
print(d3)


# A beter way 
d4 = dict(zip(l6,l7))
print(d4)


#Write a dictionary comprehension that key becomes value and value becomes key
d1 = {101:"gfg", 103:"practice", 102:"ide"}
d2 = {v:k for (k, v) in d1.items()}
print(d2)




