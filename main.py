


print("Добро пожаловать в заметки!\n")
def startmenu():
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
        pass
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


def createnewnote():
    print("Создание заметки.\n")
    noteTitle = input("Введите заголовок заметки: ")
    noteBody = input("Введите тело заметки: ")

    print("Заметка успешно сохранена")

startmenu()
