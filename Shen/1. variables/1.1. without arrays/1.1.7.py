# 1.1.7. Дано натуральное (целое неотрицательное) число а и целое
# положительное число d. Вычислить частное q и остаток r
# при делении а
# на d, не используя операций div и mod

a = 27
d = 2


def div(a, d):
    q = 0
    r = 0
    while a > d:
        a -= d
        q += 1
    r = a

    return q, r


print(div(a, d))
