'''
Задача 3.
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
'''
# # Вариант
# import random
# # Запрос ввода количества элементов
# N = int(input("Введите количество элементов: "))
# # Создание списка случайных чисел
# list = [random.randint(1, 10) for _ in range(N)]
# print(list)
# # Вывод списка в обратном порядке
# print("Последовательность в обратном порядке:")
# print(list[::-1])
# Вариант
# import random
# n = int(input("Введите количество элементов: "))
# def print_reverse_sequence(n):
#     if n == 0:
#         return
#     else:
#         print(random.randint(1, 10), end=' ')
#         print_reverse_sequence(n - 1)
# print("Сгенерированная последовательность:")
# print_reverse_sequence(n)
# print("\nв обратном порядке:")
# print_reverse_sequence(n)
# Вариант
def revers(num: int):
    if num==1: return "1"
    return str(num) + " " +revers(num-1)
num=int(input("введи число: "))
print(revers(num))