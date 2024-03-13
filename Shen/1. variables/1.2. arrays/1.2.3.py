# 1.2.3. Не используя оператора присваивания для массивов,
# составить фрагмент программы, эквивалентный оператору x:=y

def equality(list_1, list_2, n):
    for i in range(0, n):
        list_1[i] = list_2[i]
    return list_1


list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 1, 7, 6, 0]
n = len(list_1)
print(equality(list_1, list_2, n))
