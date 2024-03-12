# Задача 1

# 1. Создайте список с 5 элементами разных типов
# 2. Удалите третий элемент
# 3. Выведите в терминал длину списка
# 4. Поменяйте порядок следования элементов в списке
# 5. Создайте еще один список с двумя элементами
# 6. Расширьте первый список элементами второго списка
# 7. Выведите в терминал расширенный список из 6 элементов

first_list = [[1, 2, 3], True, 'abc', 5.5, {'a': 5}]

print("Safe list:", first_list)
first_list.pop(2)

print("List after remove third element:", first_list)
print("Length:", len(first_list))

first_list.reverse()
print("List after reverse:", first_list)

second_list = [1, 2]
print("Second list:", second_list)

first_list.extend(second_list)

print("List afrer extend second list:", first_list)
