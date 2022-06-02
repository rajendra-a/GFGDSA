l = [10, 20, 30]
l.reverse()
print(l)

m = [20, 30, 40, 50]
new_list = list(reversed(m))

n = [30, 40, 50]
new_l = n[::-1]
print(new_l)


def reverse_list(l):
    s = 0 
    e = len(l)-1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s = s+1
        e = e-1

def reverse_list_2(l):
    for i in range(len(l)//2):
        l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
