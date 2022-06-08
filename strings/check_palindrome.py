def palindrome(string):
    low = 0
    high = len(string)-1
    while low > high:
        if string[low] != string[high]:
            print("No")
            break
        low = low + 1 
        high = high - 1
    else:
        print("yes")

def is_palindrome(string):
    s1 = string[::-1]
    if string == s1:
        return True
    else:
        return False


