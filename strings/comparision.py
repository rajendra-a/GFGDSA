s1 = "geeksforgeeks"
s2 = "ide"

print(ord("a")) # TO get unicode integer value
print(chr(65))   # To get char of unicode

print(s1 < s2)
print(s1 > s2)
print(s1 == s2)
print(s1 != s2)


# Format string
name = "python guides"
course = "python course"
s = "welcome %s to the python course"

# Using .format function
s1 = "Welcome {0} to the {1}".format(name, course)
print(s1)

# using f strings
s2 = "Welcome {name} to the {course}"
print(s2)

a = 10
b = 20
print(f"sum of {a} and {b} is {a+b} ")
print(f"product of {a} and {b} is {a*b}")


s1 = "ABC"
s2 = 'abc'
print(f"the lower case of {s1} is {s1.lower()}")
print(f"the uppser case of {s2} is {s2.upper()}")

# String operations
# Membership operator
s1 = "geeksforgeeks"
s2 = "geeks"
S3 = """geeks \
            geeks
"""
print(S3)
print(s2 in s1)
print(s2 not in s2)

# Concatenation
s3 = "geeks"
s4 = "forgeeks"
s5 = s3+s4
s6 = "welcome to"+s3+s4

# Find first positin of substring
print(s1.index(s2))

# Find the last position of the index
print(s1.rindex(s2))

# Find the second position of substring
print(s1.index(s2, 0, 13))
print(s1.index(s2, 2, 13))


# length of the string
print(len("geeks"))

# Change to uppercase
s7 = "geeksforgeeks"

print(s7.upper())

print(s7.islower())
print(s7.isupper())

print(s7.startswith("geeks"))
print(s7.endswith("course"))
print(s7.startswith("geeks", 1))
print(s7.endswith("geeks", 8, len(s)))

print(s7.split())

s8 = "geeks, for, geeks"
l = ["geeksforgeeks", "python", "course"]
print(s8.split(","))
print(" ".join(l))
print(",".join(l))


# strip
s8 = "---geeksforgeeks---"
print(s8.strip("-"))
print(s8.lstrip("-"))
print(s8.rstrip("-"))

# Find method used for searching substring position at first occurance in string if the substring not present in the string 
# It returns -1
s9 = "geeks for geeks"
s10 = "geeks"
print(s1.find(s2))
print(s1.find("gfg"))
n = len(s9)
print(s9.find(s2, 1, n))

# Pattern searching in python
txt = "geeks for geeks"
pat = "geeks"

pos = txt.find(pat)

while pos >= 0:
    print(pos)
    pos = txt.find(pat, pos+1)

