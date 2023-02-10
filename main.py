import json
from datetime import date
import os


global dbList
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
    print("Выберите действие\n"
          "1. Создать.\n"
          "2. Изменить.\n"
          "3. Удалить.\n"
          "4. Поиск.\n"
          "5. Показать всё")
    choice = int(input(">> "))
    choosemenu(choice)

def choosemenu(choice):
    userEnter = choice
    if userEnter == 1:
        createnewnote()
    elif userEnter == 2:
        pass
    elif userEnter == 3:
        pass
    elif userEnter == 4:
        pass
    elif userEnter == 5:
        pass
    else:
        print("Нужно выбрать пункт меню")
        startmenu()

def createDBlist():
    with open("db.json", "r") as file:
        datb = file.read()
        dbList = json.loads(datb)

def createnewnote():
    print("Создание заметки.\n")
    currentDate = f'{date.today()}'
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")
    data = {'Date': currentDate, 'Title': noteTitle, 'NoteBody': noteBody}
    loadjson = json.load(open("db.json"))
    loadjson.append(data)
    with open("db.json", "w") as file:
        json.dump(loadjson, file, indent=2, ensure_ascii=False)
    print("Заметка успешно сохранена")


startmenu()
