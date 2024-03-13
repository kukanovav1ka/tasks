# 1.1.24. Проверить, является ли заданное натуральное число n > 1
# простым.

def is_a_prime_number(n):
    d = n
    tmp = 0
    while d > 2:
        d -= 1
        if n % d == 0:
            tmp += 1
    if tmp == 0:
        print('Yes')
    else:
        print('No')


is_a_prime_number(3)
