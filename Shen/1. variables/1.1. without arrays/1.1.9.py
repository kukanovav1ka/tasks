# 1.1.9. Последовательность Фибоначчи
# определяется так: a0 = 0,
# a1 = 1, ak = ak-1 + ak-2 при k > 2.
# Дано n, вычислить an.

n = 7568

# здесь число действий это O(n) то есть линейное


def fibonachi(n):
    result = 0
    tmp1 = 0
    tmp2 = 1
    tmp = 0
    if n == 0:
        result = tmp1
    if n == 1:
        result = tmp2
    if n > 1:
        for i in range(2, n + 1):
            result = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = result

    return result


print(fibonachi(n))
