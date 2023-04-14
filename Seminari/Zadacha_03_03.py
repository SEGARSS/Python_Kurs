'''
Задача 3.
Дан список, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
'''
list = [1, 2, 9, 7, 5, 1, 4, 6, 1, 8]
count = 0
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        count += 1
print("Количество элементов массива, больших предыдущего:", count)