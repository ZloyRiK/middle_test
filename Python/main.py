from search import find
import storage as s
import add, edit, show, empty, sort, search

 
try:
    notes = s.load()
    print ("Заметки успешно загружены")
except:
    print('Не удалось загрузить файл или файл отсутствует \nСоздайте первую запись')
    empty.save()
    
help = 'Список команд: \n/show - показать все заметки \n/add - добавить новую заметку \n/find - поиск заметки по названию \n/edit - изменение и удаление данных \n/stop - сохранить данные и остановить программу \n/help - список команд'

print(help)

while True:
    comand=input('Введите команду ')
    if comand == "/stop":
        if not notes:
            print("Программа остановлена")
        else:
            try:
                sort.sorting()
            except:
                s.save()
            print("Программа остановлена. Все изменения сохранены")
        break
    elif comand== '/add':
        add.add()
    elif comand=='/show':
        show.show() # Все заметки по дате их создания
    elif comand=='/sort':
        sort.sorting()
    elif comand == '/find':
        m = int(input("Введите месяц. Для пропуска введите 0: "))
        d = int(input("Введите день.  Для пропуска введите 0: "))
        search.find(m, d)
    elif comand == '/edit':
        id = input('Введите ID записи для изменения: ')
        print('Доступные команды:'
          +'\nЗаголовок - изменить заголовок заметки'
          +'\nТекст - изменить содержимое'
          +'\nУдалить - удалить заметку по id')
        edit.edit(id)
        print ('Запись изменена')
    elif comand == '/help':
        print(help)
    else:
        print ('Неизвестная команда \nДля открытия меню команд напишите /help')