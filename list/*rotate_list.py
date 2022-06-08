def rotate(l):
    return l[1:]+l[0:1]

print(rotate([10, 20, 30, 40, 50]))

l = [10, 20, 30, 40]
l.append(l.pop(0))
print(l)


def rotatebyone(l):
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i-1] = l[i]
    l[n-1] = x

def rotate_ar_one(l):
    n = len(l)
    x = l[0]
    for i in range(0,n):
        l[i] = l[i+1]
    l[n-1] = x



def left_rotate(d, l):
    for i in range(0,d):
        l.append(l.pop(0))
    return l

m = [10, 20, 30, 40, 30]
d = 2
left_rotate(d, m)
print(m)

def rotate_arr(l,d):
    while d > 0:
        l.append(l.pop(0))
        d -= 1

def rotate(l, d):
    for i in range(0,d):
        l.append(A[i])
    del l[:d]
    return l

def rotate_list(l, d):
    for i in range(d):
        x = l[0]
        for i in range(len(l)-1):
            l[i] = l[i+1]
        l[len(l)-1] = x
    return l

# Rotate list by d places
def rotate_by(l, d):
    return l[d:] + l[:d]


from collections import deque
l = [10, 30, 40, 40, 30]
d = 2
dq = deque(l)
dq.rotate(-d)
l = list(dq)
print(l)