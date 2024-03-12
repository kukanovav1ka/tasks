# 1.1.8. Дано натуральное n, вычислить n!

n = 3


def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result


print(factorial(n))
