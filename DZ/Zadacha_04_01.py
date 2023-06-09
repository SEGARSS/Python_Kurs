'''
Задача 1.
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
'''
import random

n = int(input("Введите количество кустов: "))

# Генерируем список урожайностей для каждого куста
harvest = [random.randint(0, 10) for _ in range(n)]

max_harvest = 0

# Итерируемся по каждому кусту
for i in range(n):
    # Считаем урожай, который можно собрать с текущего куста и двух соседних с ним
    curr_harvest = harvest[i] + harvest[(i + 1) % n] + harvest[(i - 1) % n]
    # Обновляем максимальный урожай, если текущий больше
    if curr_harvest > max_harvest:
        max_harvest = curr_harvest

print(f"Максимальный урожай, который можно собрать за один заход: {max_harvest}")