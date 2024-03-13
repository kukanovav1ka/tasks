# 1.1.16. Решить предыдущую задачу, используя в
# алгоритме Евклида деление с остатком.

def euclid(a, b):
    m = a
    p = 1
    q = 0
    n = b
    r = 0
    s = 1
    while not (m == 0 or n == 0):
        if m > n:
            p = p - (m // n) * r
            q = q - (m // n) * s
            m = m % n
        else:
            r = r - (n // m) * p
            s = s - (n // m) * q
            n = n % m
    if m == 0:
        d = n
        x = r
        y = s
    else:
        d = m
        x = p
        y = q
    return d, x, y


print(euclid(7193, 2738))
