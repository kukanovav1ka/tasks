# 1.1.14. Написать модифицированный вариант алгоритма Евклида,
# использующий соотношения НОД(a,b) = НОД(a mod b, b) при a > b,
# НОД(a,b) = НОД(a, b mod a) при b > a.

# обычный алгоритм Евклида

# Будем считать, что НОД(0,0)=0. Тогда
# НОД(a,b) = НОД(a-b,b) = НОД(a,b-a);
# НОД(a,0) = НОД(0,a) = a для всех a, b > 0.

def euclid(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    if a == 0:
        nod = b
    else:
        nod = a
    return nod

# модифицированный алгоритм Евклида


a = 18


def special_euclid(a, b):
    nod = 0
    while not (a == 0 or b == 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        nod = b
    else:
        nod = a
    return nod


print(special_euclid(a, 42))
