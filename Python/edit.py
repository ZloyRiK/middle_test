from datetime import datetime
from time import strftime

import storage as s

# notes = s.load()

# id = input('Введите ID записи для изменения: ')

# print(f'\n {notes[id]}')

def edit(id):
    notes = s.load()
    value = input('Ваша команда: ').lower()
    if value == 'заголовок':
        new_value = input('Введите новое значение: ')
        notes[id]['Заголовок']=new_value
        # print(notes[id]['Заголовок'])
        notes[id]['Дата создания'] = datetime.now().strftime("%d/%m/%y %I:%M")
        print('Дата заметки обновлена')
    elif value == 'текст':
        new_value = input('Введите новое значение: ')
        notes[id]['Текст заметки']=new_value
        # print (notes[id]['Текст заметки'])
        notes[id]['Дата создания'] = datetime.now().strftime("%d/%m/%y %I:%M")
        print('Дата заметки обновлена')
    elif value == 'Удалить':
        del notes[id]
    else:
        print ("Неизвестная команда")
    s.save()

# print(edit(id))

# notes = s.load()
# print(f'\n {notes[id]}')
