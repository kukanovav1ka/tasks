# 1.12. То же, если требуется, чтобы количество операций
# (выполненных команд присваивания) было бы порядка n (не более Cn для
# некоторой константы C).

# линейная сложность

def series(n):
    result = 0.0
    factorial = 1
    for i in range(0, n + 1):
        if i != 0:
            factorial *= i
        result += 1 / factorial
        print(i, result)
    return result


print(series(9))
