import json
import sys
from datetime import date, datetime
import os


def checkDB():
    if os.path.exists('db.json'):
        createDBlist()
    else:
        temp = []
        file = open('db.json', 'w')
        file.write(json.dumps(temp, indent=2, ensure_ascii=False))
        file.close()


print("Добро пожаловать в заметки!\n")


def startmenu():
    checkDB()
    choice = int(input("Выберите действие\n"
                       "1. Создать.\n"
                       "2. Поиск.\n"
                       "3. Показать всё\n"
                       "4. Выйти\n"))
    choosemenu(choice)


def choosemenu(choice):
    userEnter = choice
    if userEnter == 1:
        createnewnote()
    elif userEnter == 2:
        searchMenu()
    elif userEnter == 3:
        showallNotes()
    elif userEnter == 4:
        sys.exit()
    else:
        print("Нужно выбрать пункт меню")
        startmenu()


def createDBlist():
    global dbList
    with open("db.json", "r") as file:
        datb = file.read()
        dbList = json.loads(datb)


def createnewnote():
    print("Создание заметки.\n")
    currentDatetime = datetime.now()
    currentDate = f'{currentDatetime.day}.{currentDatetime.month}.{currentDatetime.year}'
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")
    data = {'Date': currentDate, 'Title': noteTitle, 'NoteBody': noteBody}
    loadjson = json.load(open("db.json"))
    loadjson.append(data)
    with open("db.json", "w") as file:
        json.dump(loadjson, file, indent=2, ensure_ascii=False)
    print("Заметка успешно сохранена")


def changeNote():
    pass


def delNote():
    pass


def searchMenu():
    userEnter = int(input('Выберите критерии для поиска:\n'
                          '1. По дате\n'
                          '2. По заголовку\n'
                          '3. В главное меню\n'))
    if userEnter == 1:
        findByDate()
    if userEnter == 2:
        findByTitle()
    if userEnter == 2:
        startmenu()


def findByDate():
    userEnter = input('Введите дату формата day.month.year')
    for item in dbList:
        if item['Date'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
        else:
            print('Заметки с такой датой не существует')

    subMenu()


def findByTitle():
    userEnter = input('Введите дату формата day.month.year')
    for item in dbList:
        if item['Date'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
        else:
            print('Заметки с такой датой не существует')

    subMenu()


def showallNotes():
    for item in dbList:
        print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
    startmenu()


def subMenu():
    userEnter = int(input('Что делаем дальше?\n'
                          '1. Изменить\n'
                          '2. Удалить\n'
                          '3. В главное меню\n'))
    if userEnter == 1:
        pass
    elif userEnter == 2:
        pass
    elif userEnter == 3:
        startmenu()


startmenu()
