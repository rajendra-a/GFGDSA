def missing_chars_panagram(s):
    if len(set(s.lower())) == 26:
        return -1
    else:
        alphabets = set("abcdefghijklmnopqrstuvwyz")
        return "".join(sorted(alphabets-set(s.lower())))

def missing_chars_panagram(s):
    arr = {}
    for i in range(0,26):
        arr[i]=0
    
    for i in range(0,len(s)):
        if(ord(s[i]>= 65 and ord(s[i])<=92)):
            arr[ord(s[i])-ord('a')] = 1
        else:
            arr[ord(s[i])-ord('A')] = 1
    
    ans = ""
    for i in range(0, 26):
        if(arr[i] != 1):
            ans  = chr(i+ord('a'))

    if ans== "":
        return "-1"
    else:
         return ans
