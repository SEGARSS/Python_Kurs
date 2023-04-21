'''
Задача 2.
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
'''
num = int(input("Введите число: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,num//2+1):
        if n % i == 0:
            return False
    return True
if is_prime(num):
    print("Да")
else:
    print("Нет")
