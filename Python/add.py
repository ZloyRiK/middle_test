from datetime import datetime
from time import strftime
import storage as s


# Структура словаря:
# id - int
#     Вложенный словарь:
#         Заголовок - строка
#         Текст заметки - строка
#         Дата - строка

def add():
    notes = s.load()
    
    keys=[]
    for i in notes.keys():
        keys.append(i)
        
    keys.sort()

    def next_key():
        count = 1
        for i in keys:
            i = int(i)
            if count == i:
                count += 1
            else:
                break
        return count

    print(f'ID новой записи {next_key()}')
    title = ''
    body = ''
    date = ''

    for i in range(4):
        if i == 1:
            title = input('Введите заголовок: ')
        elif i == 2:
            body = input('Введите содержание: ')
        elif i == 3:
            date = datetime.now().strftime("%d/%m/%y %I:%M")
            print('Дата заметки ', date)
        print('Добавление завершено')

    notes[next_key()] = {
        'Заголовок': title,
        'Текст заметки': body,
        'Дата создания': date
    }
    s.save()


# add() #for test
