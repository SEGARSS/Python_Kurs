'''
Задача 0.
Напишите программу, 
которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
'''
num = int(input("Введите число: "))
step = int(input("Введите степень: "))
def power(num, step):
    if step == 0:
        return 1
    elif step % 2 == 0:
        temp = power(num, step // 2)
        return temp * temp
    else:
        return num * power(num, step-1)
result = power(num, step)
print(f"{num} в степени {step} равно {result}")