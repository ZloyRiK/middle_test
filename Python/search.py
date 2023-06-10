import storage as s

# Команда /find


def find(month, day):
    notes = s.load()
    if month != 0 or day != 0:
        for k, info in notes.items():
            title = info['Заголовок']
            body = info['Текст заметки']
            date = info['Дата создания']
            if month == int(date.split('/')[1]) or month == 0:
                if day == int(date.split('/')[0]) or day == 0:
                    print(f'id {k}: \n{title} \n{body} \n{date}')
            else:
                print("Заметок за эту дату не найдено")

# find(6, 0)
