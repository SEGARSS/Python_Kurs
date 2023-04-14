'''
Задача 2.
Напишите программу для печати всех уникальных
значений в словаре.
'''
list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
        {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
        {" VIII ":" S007 "}]

unique_values = set()
for d in list:
    for value in d.values():
        unique_values.add(value.strip())

print(unique_values)