# 1.1.6. Даны натуральные числа а и b. Вычислить их сумму а + b.
# Использовать операторы присваивания лишь вида
# переменная1 := переменная2,
# переменная := число,
# переменная1 := переменная2 + 1


a = 4
b = 5


def sum(a, b):
    result = a
    k = 0
    while k != b:
        result += 1
        k += 1
    return result


print(sum(a, b))