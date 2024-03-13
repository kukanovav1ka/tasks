# 1.1.21. Та же задача, но разрешается использовать из
# арифметических операций лишь сложение и вычитание,
# причём общее число действий должно быть порядка n.

def square(n):
    number_square = 0
    for i in range(0, n + 1):
        if i == 0:
            number_square = 0
        else:
            number_square = number_square + i - 1 + i
        print(number_square)


def square_without_minus(n):
    number_squre = 0
    i = 0
    print(0)
    while not i == n:
        number_squre = number_squre + i
        i = i + 1
        number_squre = number_squre + i
        print(number_squre)


square_without_minus(10)
