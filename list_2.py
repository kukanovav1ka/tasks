# Задача 2

# 1. Создайте два списка
# 2. Объедините два списка, используя оператор +
# 3. Определите, какой магический метод списков вызывается при использовании оператора +
# 4. Выполните слияние списков, используя этот магический метод
# 5. Результат выведите в терминал


first_list = [1, 2, 3, 4]
print("First list:", first_list)

second_list = [5, 6, 7]
print("Second list:", second_list)

merge_list = first_list + second_list
print("Merge list:", merge_list)
print("Other merge list:", first_list.__add__(second_list))
