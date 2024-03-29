# 1.1.18. Написать вариант алгоритма Евклида, использующий соотношения
# НОД(2a, 2b) = 2 · НОД(a, b),
# НОД(2a, b) = НОД(a, b) при нечётном b,
# не включающий деления с остатком, а использующий лишь деление на 2
# и проверку чётности. (Число действий должно быть порядка log k для
# исходных данных, не превосходящих k.)


def euclid(a, b):
    m = a
    n = b
    d = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            d *= 2
            m = m // 2
            n = n // 2
        elif m % 2 == 0 and n % 2 == 1:
            m = m // 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
        else:
            if m > n:
                m = m - n
            else:
                n = n - m
    if m == 0:
        d *= n
    else:
        d *= m
    return d


print(euclid(49, 21))
