'''
Задача 1.
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
'''
text = input("Введите текст: ")

# Разделяем текст на слова и помещаем их в множество
words_set = set(text.split())

# Выводим количество уникальных слов в тексте
print("Количество уникальных слов в тексте:", len(words_set))
