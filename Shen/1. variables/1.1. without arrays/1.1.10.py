# 1.1.10. Та же задача, если требуется, чтобы число
# операций было пропорционально log n.
# (Переменные должны быть целочисленными.)

n = 7


def multiplay_matrix(a, b, m):
    result = []
    for t in range(0, m * m):
        result.append(0)
    for j in range(0, m):
        for i in range(0, m):
            for k in range(0, m):
                result[i * m + j] += a[i * m + k] * b[k * m + j]

    return result


def degree(x, n, m):
    result = []
    if n == 0:
        result.append(1)
        result.append(0)
        result.append(0)
        result.append(1)
    elif n == 1:
        result = x
    else:
        result = degree(x, n // 2, m)
        result = multiplay_matrix(result, result, m)
        if n % 2 != 0:
            result = multiplay_matrix(x, result, m)
    return result


def fibonachi(n):
    matrix = degree([1, 1, 1, 0], n, 2)
    Fn = matrix[1]
    return Fn


print(fibonachi(n))
