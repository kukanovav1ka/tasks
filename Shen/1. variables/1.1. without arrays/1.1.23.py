# 1.1.23. Составить программу решения предыдущей задачи,
# использующую тот факт, что составное число имеет делитель,
# не превосходящий квадратного корня из этого числа.

def simple_decomposition(n):
    p = 2
    while not n == 1:
        if n % p == 0:
            n = n / p
            print(p)
        elif p * p > n:
            p = n
        else:
            p += 1


n = 882
if n > 1:
    simple_decomposition(n)
