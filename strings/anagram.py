# What is anagram
# Anagram is word formed by rearranging the letters of different or word
def are_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return (s1==s2)

def are_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True
def are_anagram2(str1, str2):
    if len(s1) != len(s2):
        return False
    mp = {}
    for i in a:
        if i in mp.keys():
            mp[i] += 1
        else:
            mp[i] = 1
    
    for i in b:
        if i not in mp.keys():
            return False
        else:
            mp[i] -= 1
    
    for i in mp.keys():
        if mp[i] != 0:
            return False
    return False

def are_anagram1(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in s1:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in letter:
        if count[k] != 0:
            return False
    return True