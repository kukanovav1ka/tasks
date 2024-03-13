# 1.1.19. Дополнить алгоритм предыдущей задачи поиском x и y, для
# которых ax + by = НОД(a, b).

def euclid(a, b):
    d = 1
    m = a
    p = 1
    q = 0
    n = b
    r = 0
    s = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            d *= 2
            m = m // 2
            n = n // 2
        elif m % 2 == 0 and n % 2 == 1:
            m = m // 2
            p *= 2
            q *= 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
            r *= 2
            s *= 2
        else:
            if m > n:
                m = m - n
                p = p - r
                q = q - s
            else:
                n = n - m
                r = r - p
                s = s - q
    if m == 0:
        d *= n
        x = r
        y = s
    else:
        d *= m
        x = p
        y = q
    return d, x, y
