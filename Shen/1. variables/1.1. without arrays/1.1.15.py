# 1.1.15. Даны натуральные a и b, не равные 0 одновременно.
# Найти d = НОД(a,b) и такие целые x и y, что d = a · x + b · y.

def euclid(a, b):
    m = a
    p = 1
    q = 0
    n = b
    r = 0
    s = 1
    while not (m == 0 or n == 0):
        if m > n:
            m = m - n
            p = p - r
            q = q - s
        else:
            n = n - m
            r = r - p
            s = s - q
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
