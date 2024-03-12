# Задача

# 1. Создайте пустой словарь
# 2. Трижды попросите пользователя сначала ввести название
# ключа, а потом ввести значение для этого ключа. Всего
# должно быть 6 запросов на ввод текста.
# 3. Во время получения данных от пользователя добавляйте
# в словарь ключи с значениями согласно тому, что ввел пользователь
# 4. Выведите результирующий словарь в терминал.
# 5. Добавить два ключа в этот словарь со значениями, а также
# удалить два ключа и вывести на экран, что получилось.

dict = {}

key_1 = input("Enter key one: ")
mean_1 = input("Enter mean one: ")
dict[key_1] = mean_1

key_2 = input("Enter key two: ")
mean_2 = input("Enter mean two: ")
dict[key_2] = mean_2

key_3 = input("Enter key three: ")
mean_3 = input("Enter mean three: ")
dict[key_3] = mean_3

print("Dictionary after added user's keys:", dict)

dict['d'] = '4'
dict['e'] = '5'

print("Dictionary after added my keys:", dict)

del dict[key_1]
del dict[key_2]

print("Dictionary after delete keys:", dict)
