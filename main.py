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


def startmenu():  # Главное меню
    checkDB()
    choice = int(input("Выберите действие\n"
                       "1. Создать.\n"
                       "2. Поиск.\n"
                       "3. Показать всё\n"
                       "4. Выйти\n"))
    choosemenu(choice)


def choosemenu(choice):  # Метод проверяющий выбор пользователя
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


def createDBlist():  # Создаем список из файла db.json
    global dbList
    with open("db.json", "r") as file:
        datb = file.read()
        dbList = json.loads(datb)


def checkDate():  # Проверяем дату.
    currentDatetime = datetime.now()
    month = currentDatetime.month
    if month < 10:
        month = f'0{month}'
    currentDate = f'{currentDatetime.day}.{month}.{currentDatetime.year}'
    return currentDate


def createnewnote():  # Метод создания заметки
    print("Создание заметки.\n")
    currentDate = checkDate()
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")
    data = {'Date': currentDate, 'Title': noteTitle, 'NoteBody': noteBody}
    loadjson = json.load(open("db.json"))
    loadjson.append(data)
    with open("db.json", "w") as file:
        json.dump(loadjson, file, indent=2, ensure_ascii=False)
    print("Заметка успешно сохранена\n")
    startmenu()


def changeNote(tempDict):  # Метод изменения заметки
    newList = []
    currentDate = checkDate()
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")
    data = {'Date': currentDate, 'Title': noteTitle, 'NoteBody': noteBody}
    for item in dbList:
        if item == tempDict:
            newList.append(data)
        else:
            newList.append(item)
    with open("db.json", "w") as file:
        json.dump(newList, file, indent=2, ensure_ascii=False)
    print("Заметка успешно изменена\n")
    startmenu()


def delNote(tempDict):  # Метод удаления заметки
    newList = []
    for item in dbList:
        if item == tempDict:
            pass
        else:
            newList.append(item)
    with open("db.json", "w") as file:
        json.dump(newList, file, indent=2, ensure_ascii=False)
    print("Заметка успешно удалена\n")
    startmenu()


def searchMenu():  # Меню поиска
    userEnter = int(input('Выберите критерии для поиска:\n'
                          '1. По дате\n'
                          '2. По заголовку\n'
                          '3. В главное меню\n'))
    if userEnter == 1:
        findByDate()
    elif userEnter == 2:
        findByTitle()
    elif userEnter == 2:
        startmenu()


def findByDate():  # Поиск по дате
    temp = {}
    userEnter = input('Введите дату формата day.month.year')
    for item in dbList:
        if item['Date'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            temp = item
        else:
            print('Заметки с такой датой не существует')

    subMenu(temp)


def findByTitle():  # Поиск по заголовку
    userEnter = input('Введите заголовок заметки: ')
    temp = {}
    for item in dbList:
        if item['Title'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            temp = item
        else:
            print('Заметки с такой датой не существует')

    subMenu(temp)


def showallNotes():  # Метод, показывающий весь список заметок
    for item in dbList:
        print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
    startmenu()


def subMenu(temp):  # Под-меню, после выполненных функций
    userEnter = int(input('Что делаем дальше?\n'
                          '1. Изменить\n'
                          '2. Удалить\n'
                          '3. В главное меню\n'
                          '4. Выйти\n'))
    if userEnter == 1:
        changeNote(temp)
    elif userEnter == 2:
        delNote(temp)
    elif userEnter == 3:
        startmenu()
    elif userEnter == 4:
        sys.exit()
    else:
        print('Нужно выбрать пункт меню')


startmenu()
