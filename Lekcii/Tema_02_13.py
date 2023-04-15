# Самые распространенные ошибки при работе с Python:
# SyntaxError(Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second # !!!!!
print(number_first)
# Отсутствие символа - (:) - а правильно так - if number_first > number_second:
print("==================")
# IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!
''' Отсутствие отступов - должно быть так - 
if number_first > number_second:
    print(number_first)
'''
print("==================")
# TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number),
'''Нельзя складывать строки и числа, должно быть так -
print(number + number)
или
print(text + text)
'''
print("==================")
# ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя
print("==================")
# KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует print(dictionary[3]) - мы можем запросить print(dictionary[1]) или print(dictionary[2])
print("==================")
# NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует, мы объявили только name, её и можем запросить - print(name).
print("==================")
# ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения и наоброт.