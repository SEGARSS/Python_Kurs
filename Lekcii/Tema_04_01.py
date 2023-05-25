'''
Функция map
Функция map() применяет указанную функцию к каждому элементу
итерируемого объекта и возвращает итератор с новыми объектами.
'''
data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
'''
map() позволит избавиться от функции select.
Теперь вернемся к задаче. С помощью функции map():
'''
data = list(map(int,input().split()))
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
