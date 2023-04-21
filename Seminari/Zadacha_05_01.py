'''
Задача 1.
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
'''
import random
num=10
array=[]
for i in range(num):array.append(random.randint(1,5))
print(array)
max_point=max(array)
min_point=min(array)
for i in range(num):
    if array[i]==max_point:
        array[i]=min_point
print(array)