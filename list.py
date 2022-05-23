l = [10, 20, 30, 40, 50]

# Print list
print(l)

# Access elements from list
print(l[3])
print(l[-1])
print(l[-2])

# Append method append object to the end the list
l.append(60)
l.append(40)

# Insert function inserts item at the given index
l.insert(1, 15)

# In operator in python tells you weather an item present in collection or not
print(15 in l)

# Count funtion tells you how many occurences of the value are present in the given sequece
print(l.count(30))

# Index method tells you index of first occurence of value
print(l.index(50))
# If item not present in the given index it raises an error
print(l)
# It searches for element from the index 5 to 7
print(l.index(50, 5 ,7))



# Removal of items from list
# Remove function remove the first occurance from the list, if the item to remove is not present in the list 
# it raises an error 
l.remove(20)

# Now look at modified list
print(l)

# Pop function remove the last item from the list
# If value not present in the list it raises IndexError if list is empty or index is out of range
l.pop()

l.pop(2)


# We can use del keyword to delete the value from the list
# it deletes target list recursively, deletes each target from index  to to index
print(l)
del l[1]

del l[:2]
print(l)

l1 = [10, 40, 20, 50]

# maximum value from the iterable or any number of iterables; can be more than one 
# key: function where the iterables are passed and comparision is performed based on its returned value
# default:  default value if the given iterable is empty 
print(max(l1))

print(max([12, 23, 55], [46, 56, 90], [92, 23, 55], [45, 57, 93]))

# minimum value from the iterable or any number of iterables; can be more than one 
# key: function where the iterables are passed and comparison is performed based on its returned value
# default: default va;ue of the givem iterable is empty

print(min([1, 4, 6, 8, 9, 23, 45, 33, 22, 26])) 



# sum: sum function return sum of an iterable object
print(sum([2, 3, 5, 8, 2]))

lst1 = [50, 45, 34, 34, 57, 34, 45, 9]
# reverse: reverse function reverse the iterable
lst1.reverse()
print(lst1)

lst1.sort()
print(lst1)


