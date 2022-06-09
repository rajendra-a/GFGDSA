def panagram_checking(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if set(s.lower()) == alphabets:
        return 1
    else:
        return 0
    


def is_panagram(s):
    if len(s) < 26:
        return False
    else:
        ret = 1
        a = [chr(i) for i in range(97, 123)]
        for item in a:
            if (item not in s) and (item.upper() not in s):
                ret = 0
                break
    return ret


    