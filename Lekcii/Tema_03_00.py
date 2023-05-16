'''
Функция. Её создание, передача и работа.
'''
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

n = int(input("Введите число: ")) # 5
print(sumNumbers(n)) # 15