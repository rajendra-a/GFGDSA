def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def fibonacci_series(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def max_number_from_list(l):
    m = l[0]
    for x in l:
        if x > m:
            m = x
    return m

print(max_number_from_list([1, 2, 3, 14, 5, 6, 7, 8, 9, 10]))


# write a program for check the number is fibonacci or not
def fibonacci_number(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()