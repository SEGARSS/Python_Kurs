'''
Функция filter
Функция filter() применяет указанную функцию к каждому элементу
итерируемого объекта и возвращает итератор с теми объектами, для которых
функция вернула True.
'''
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]
'''
filter() позволит избавиться от функции where, которую мы писали ранее
'''
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

