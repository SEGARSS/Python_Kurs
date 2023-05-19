'''
Задача 2.
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
'''
def same_by(characteristic, objects):
    if not objects:
        return True

    first_characteristic = characteristic(objects[0])
    for obj in objects:
        if characteristic(obj) != first_characteristic:
            return False

    return True

def get_length(word):
    return len(word)

words = ['apple', 'banana', 'cherry']
result = same_by(get_length, words)
print(result)