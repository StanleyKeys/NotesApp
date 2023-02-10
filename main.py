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

def checkDate():
    currentDatetime = datetime.now()
    month = currentDatetime.month
    if month < 10:
        month = f'0{month}'
    currentDate = f'{currentDatetime.day}.{month}.{currentDatetime.year}'
    return currentDate
def createnewnote():
    print("Создание заметки.\n")
    currentDate = checkDate()
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")
    data = {'Date': currentDate, 'Title': noteTitle, 'NoteBody': noteBody}
    loadjson = json.load(open("db.json"))
    loadjson.append(data)
    with open("db.json", "w") as file:
        json.dump(loadjson, file, indent=2, ensure_ascii=False)
    print("Заметка успешно сохранена")


def changeNote(tempDict):
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
    print("Заметка успешно изменена")

def delNote(tempList):
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
    temp = {}
    userEnter = input('Введите дату формата day.month.year')
    for item in dbList:
        if item['Date'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            temp = item
        else:
            print('Заметки с такой датой не существует')

    subMenu(temp)


def findByTitle():
    userEnter = input('Введите заголовок заметки: ')
    temp = {}
    for item in dbList:
        if item['Title'] == userEnter:
            print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            temp = item
        else:
            print('Заметки с такой датой не существует')

    subMenu(temp)


def showallNotes():
    for item in dbList:
        print(f"\nДата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
    startmenu()


def subMenu(temp):
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
