# Check if list is sorted or not
def sorted_list(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i + 1
    return True

print(sorted_list([0, 30, 40, 10, 50]))


def is_sorted(l):
    sl = sorted(l)
    if sl == l:
        return True
    else:
        return False

def isSorted(self,arr,n):
        #code here
        i = 1
        while i<n:
            if arr[i]<arr[i-1]:
                break
            i += 1
        j = 1
        while j<n:
            if arr[j]>arr[j-1]:
                break
            j += 1
        if i == n or j == n:
            return 1
        return 0


print(all(l[i] <= l[i+1] for i in range(len(l-1))))


