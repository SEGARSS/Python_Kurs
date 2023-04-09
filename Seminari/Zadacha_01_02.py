"""
Задача. Вагоны в электричке пронумерованы натуральными числами, 
начиная с 1 
(при этом иногда вагоны нумеруются от «головы» поезда, 
а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
В каждом вагоне написан его номер. 
Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
Он хочет определить, сколько всего вагонов в электричке. 
Напишите программу, которая будет это делать или сообщать, 
что без дополнительной информации это сделать невозможно.
"""
# Первый вариант
j = int(input("Введите номер вагона, в котором сидит Витя: "))
i = int(input("Введите порядковый номер вагона от головы поезда: "))
n = abs(i - j)
print("Количество вагонов в электричке:", n)
# Второй вариант
j = int(input("Введите номер вагона, в котором сидит Витя: "))
i = int(input("Введите порядковый номер вагона от головы поезда: "))
n = 0
if j < i:
    n = i - j + 1
else:
    n = j - i + 1
print("Количество вагонов в электричке:", n)