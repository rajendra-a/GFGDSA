lst = [10, 20, 30, 40, 50]

# print list of elements from index 0 to 5 
print(lst[0:5:2])
print(lst[:4])
print(lst[2:])
print(lst[1:4])
print(lst[4:1:-1])   # When you do negative step your start must greater than stop other wise will get empty list
print(lst[-1:-6:-1])  # -1 is greater than -6 so here we don't get empty list
print(lst[-6:-1])   
print(lst[4:1]) # When the start item is greater than stop it will give you empty list 
print(lst[1:4:-1])  # when you have smaller element as start and have negative step it will also give empty list


# copying list, tuple, string
lst1 = [10, 20, 30, 40]
lst2 = lst1[:]
lst3 = [10, 20, 30, 40]
# when we sliced the list it will give you a new copy of list not the same as the list defined previously
# becuase list is mutable
print(lst1 is lst2)
print(lst1 is lst3)

tuple1 = (10, 20, 30)
tuple2 = tuple1[:]
tuple3 = (10, 20, 30)
# when we sliced a tuple it will give you a copy of already defined tuple
# because tuple is immutable
print(tuple1 is tuple2)
print(tuple1 is tuple3)

str1 = "string"
str2 = str1[:]
str3 = "string"

# When you sliced a string it will give you a copy of already defined string
print(str1 is str2)
print(str1 is str3)

