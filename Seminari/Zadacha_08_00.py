# Задача 49
# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def file_read(f_name) -> list:  # считывание данных файла в данные
    data = open(f_name).read().split('\n')
    return [i.split(':') for i in data]

def file_write(f_name, data: list) -> None:  # запишите данные в указанный файл
    data = [':'.join(map(str, data[i])) for i in range(len(data))]
    open(f_name, 'w').writelines('\n'.join(map(str, data)))

def show_records(data: list, fields: list, elem_show=[-1]) -> None: # распечатайте список по указанным индексам
    if elem_show[0] == -2: # нечего показывать - ценность сервиса
        print("По этому запросу не найдено записей!\n")
    else:
        if elem_show[0] == -1:  # по умолчанию -> распечатать все данные
            elem_show = range(len(data))
            print("\nВСЕ ЗАПИСИ:")
        else:
            print("\nНАЙДЕННЫЕ ЗАПИСИ:")

        print('\t '.join(fields))
        print("⸻" * 60)
        print('\n'
            .join(map(str, [data[i] for i in elem_show]))
            .replace("[", "")
            .replace("]", "")
            .replace('\'', "")
            .replace(",", "\t\t"))

def add_record(data: list, fields: list) -> list: # добавить контакт в набор данных
    print("\nДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ:")
    new_line = [input(f"войдите в {fields[i]}:\t") for i in range(len(fields))]
    data.append(new_line)
    return data

def find_record(data: list) -> list: # добавить контакт в набор данных, найти все записи, соответствующие критериям
    search_val = input(f"\nВведите значение для поиска\n(имя, фамилия, номер телефона, комментарий или их комбинация разделяются пробелом): ").split()
    res = [x for x in range(len(data)) if all(map(lambda v: v in data[x], search_val))]

    if len(res) == 0:
        res = [-2]

    return res

def modify_record(data: list, fields: list) -> list: # измените запись, найденную по критериям
    print("\nРЕЖИМ ИЗМЕНЕНИЯ ЗАПИСИ")

    rec_modify = [-1]
    while rec_modify[0] < 0 or len(rec_modify) > 1:
        rec_modify = find_record(data)
        show_records(data, fields, rec_modify)
        if len(rec_modify) > 1:
            print("\nБолее 1 записи соответствует вашему запросу - используйте несколько полей для указания!")

    fld_modify = int(input(f"\nКакое поле вы хотели бы изменить (1-5)?\n(1 - фамилия, 2 - имя, 3 - номер телефона, 4 - комментарий, 5 - БЕЗ изменений): ")) - 1

    if 0 <= fld_modify < 5:
        data[rec_modify[0]][fld_modify] = input(f"Введите новое значение для поля \'{fields[fld_modify]}\' для замены текущего значения \'{data[rec_modify[0]][fld_modify]}\': ")

    return data

def delete_record(data: list, fields: list) -> list: # измените запись, найденную по критерию, и удалите запись, найденную по критерию
    print("\nРЕЖИМ УДАЛЕНИЯ ЗАПИСИ")

    rec_modify = [-1]
    while rec_modify[0] < 0 or len(rec_modify) > 1:
        rec_modify = find_record(data)
        show_records(data, fields, rec_modify)
        if len(rec_modify) > 1:
            print("\nБолее 1 записи соответствует вашему запросу - используйте несколько полей для указания!")

    del_confirm = input("\nПодтвердите, что вы хотели бы удалить указанную выше запись (Y/N): ")

    if del_confirm == 'Y' or del_confirm == 'y':
        data.pop(rec_modify[0])

    return data


file_name = 'phones.txt'
data_fields = ['фамилия', 'имя', 'номер телефона', 'комментарий']
data = file_read(file_name)

while 1:

    print('''
    КОМАНДЫ ДЛЯ ТЕЛЕФОННОЙ КНИГИ:
    Просмотр всех записей - 1
    Поиск записи - 2
    Добавление новой записи - 3
    Удаление записи - 4
    Изменение записи - 5
    Выход - 0 ''')

    command = int(input('\nВыберите свою команду: '))
    if command == 1: #показать все записи
        show_records(data, data_fields)
    elif command == 2: # показать найденные записи
        show_records(data, data_fields, find_record(data))
    elif command == 3: #добавить запись
        add_record(data, data_fields)
    elif command == 4: #удалить запись
        delete_record(data, data_fields)
    elif command == 5: #удалить запись
        modify_record(data, data_fields)
    elif command == 0: #сохранить и выйти
        file_write(file_name, data)
        break
    else:
       print('\nКоманда НЕ существует! Пробовать снова.')
