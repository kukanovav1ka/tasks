# 1.1.20. Составить программу, печатающую квадраты всех
# натуральных чисел от 0 до заданного натурального n

def square(n):
    for i in range(0, n + 1):
        print(i * i, end=',')
    print()


n = int(input())
square(n)
