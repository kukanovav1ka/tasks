# 1.1.5. Даны натуральные числа а, b. Вычислить произведение a · b,
# используя в программе лишь операции +, -, =, <>.

a = 4
b = 5


def multiplication(a, b):
    result = 0
    while b != 0:
        result += a
        b -= 1
    return result


print(multiplication(a, b))
