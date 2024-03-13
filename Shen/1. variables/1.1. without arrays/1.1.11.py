# 1.1.11. Дано натуральное n, вычислить
# 1 / 0! + 1 / 1! + . . . + 1 / n!.

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

# квадратичная сложность


def series(n):
    result = 0.0
    for i in range(0, n + 1):
        result += 1 / factorial(i)
        print(i, result)
    return result


print(series(9))
