import storage as s  

def show():
    notes = s.load()
    for k, v in notes.items():
            title=v['Заголовок']
            body = v['Текст заметки']
            date = v['Дата создания']
            print (f'ID {k} \nЗаголовок: {title} \nТекст заметки: {body} \nДата создания: {date}')