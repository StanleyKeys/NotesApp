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
    else:
        print('Нужно выбрать пункт меню')
        searchMenu()


def findByDate():  # Поиск по дате
    tempList = []
    userEnter = input('Введите дату в формате день.месяц.год:  ')
    dateList = userEnter.split(".")
    if len(dateList) != 3:
        print('Дата введена неверно. Попробуйте еще раз.\n')
        findByDate()
    else:
        pass

    id = 1
    for item in dbList:

        if item['Date'] == userEnter:
            print(f"Заметка № {id}")
            print(f"Дата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            tempList.append(item)
            id += 1
        else:
            print('Заметки с такой датой не существует')

    subMenu(tempList)


def findByTitle():  # Поиск по заголовку
    userEnter = input('Введите заголовок заметки: ')
    tempList = []
    id = 1
    for item in dbList:

        if item['Title'] == userEnter:
            print(f"Заметка № {id}")
            print(f"Дата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
            tempList.append(item)
            id += 1
        else:
            print('Заметки с таким заголовком не существует')

    subMenu(tempList)


def showallNotes():  # Метод, показывающий весь список заметок
    id = 1
    for item in dbList:
        print(f"Заметка № {id}")
        print(f"Дата: {item['Date']}\nЗаголовок: {item['Title']}\nТекст: {item['NoteBody']}\n")
        id += 1
    startmenu()


def subMenu(tempList):  # Под-меню, после выполненных функций
    userEnter = int(input('Что делаем дальше?\n'
                          '1. Изменить\n'
                          '2. Удалить\n'
                          '3. В главное меню\n'
                          '4. Выйти\n'))
    if userEnter == 1:
        if len(tempList) == 1:
            changeNote(tempList[0])
        else:
            changeMenu(tempList)
    elif userEnter == 2:
        if len(tempList) == 1:
            delNote(tempList[0])
        else:
            delMenu(tempList)

    elif userEnter == 3:
        startmenu()
    elif userEnter == 4:
        sys.exit()
    else:
        print('Нужно выбрать пункт меню')


def changeMenu(tempList):  # Под-меню для изменения (в случае если заметок несколько)
    userNumber = int(input('Найдено несколько заметок. Какую заметку меняем?\n'))
    changeNote(tempList[userNumber])


def delMenu(tempList):  # Под-меню для удаления (в случае если заметок несколько)
    userNumber = int(input('Найдено несколько заметок. Какую заметку удаляем?\n'))
    delNote(tempList[userNumber])


startmenu()
