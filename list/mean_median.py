def mean(l):
    return sum(l)/len(l)

def medain(l):
    l.sort()
    if len(l)%2 == 0:
        return l[len(l)//2-1]
    else:
        return l[len(l)//2]