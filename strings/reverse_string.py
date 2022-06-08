def reverse(string):
    rev =""
    for i in string:
        rev = i + rev
    print(rev)

def reverse1(string):
    return string [::-1]

