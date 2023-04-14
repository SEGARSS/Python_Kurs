'''
Задача 1.
Требуется найти в списке List[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
В последующих строках записаны N целых чисел List i. Последняя строка содержит число X
'''
import random
n = int(input("Введите количество элементов с писке: "))
list = [random.randint(1,1000)for i in range(n)]
print(*list)
x = int(input("Введите число x: "))
min_diff = abs(list[0])
closest_elem = list[0]
for elem in list:
    if abs(elem - x) < min_diff:
        min_diff = abs(elem - x)
print(f"Самый близкий к числу {x} элемент в списке {list} равен {closest_elem}")
