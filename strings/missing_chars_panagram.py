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
        if(ord(s[i] >= 65 and ord(s[i]) <= 92)):
            arr[ord(s[i])-ord('a')] = 1
        elif (ord(s[i] >= 97 and ord(s[i]) <= 122)):
            arr[ord(s[i])-ord('A')] = 1
    
    missing_chars = ""
    for i in range(0, 26):
        if(arr[i] != 1):
            missing_chars  += chr(i+ord('a'))

    if missing_chars== "":
        return "-1"
    else:
         return missing_chars
