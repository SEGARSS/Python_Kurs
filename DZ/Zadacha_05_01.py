'''
Задача 1.
Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
'''
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def sum(a, b):
    # базовый случай - одно из чисел равно 0
    if a == 0:
        return b
    if b == 0:
        return a
    # рекурсивный случай - складываем два числа, 
    # одновременно уменьшая каждое на 1
    return sum(a-1, b) + 1
print(sum(a-1, b) + 1)    