'''
Возможность передачи неограниченного количества аргументов
● Можно указать любое количество значений аргумента функции.
● Перед аргументом надо поставить *.
'''
def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1