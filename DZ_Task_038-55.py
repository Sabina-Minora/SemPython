"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных."""

phonedirectory = {}

def add_contact(name, phone):
    #Добавление контакта в телефонную книгу
    phonedirectory[name] = phone
    update_file()

def update_contact(name, new_phone):
    #Обновление номера телефона для существующего контакта
    if name in phonedirectory:
        phonedirectory[name] = new_phone
        update_file()
    else:
        print(f"{name} не найден в телефонной книге.")

def delete_contact(name):
    #Удаление контакта из телефонной книги
    if name in phonedirectory:
        del phonedirectory[name]
        update_file()
    else:
        print(f"{name} не найден в телефонной книге.")

def print_phonedirectory():
    #Печать содержимого телефонной книги
    if phonedirectory:
        print("Телефонная книга: \n")
        for name, phone in phonedirectory.items():
            print(f"{name}: {phone}")
    else:
        print("Телефонная книга пуста.")

def update_file():
    #Запись данных в файл
    with open("phonedirectory.txt", "w") as file:
        for name, phone in phonedirectory.items():
            file.write(f"{name}: {phone}\n")

def load_data_from_file():
    #Чтение данных из файла
    try:
        with open("phonedirectory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone = line.strip().split(": ")
                phonedirectory[name] = phone
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist

#Загрузка данных из файла при запуске программы
load_data_from_file()

#Добавление одного контакта
print("Добавление контакта:")
name = input("Фамилия Имя Отчество: ")
phone = input("Номер телефона: ")
add_contact(name, phone)

#Меню с функциями
while True:
    print("\nМеню:")
    print("1. Печать телефонной книги")
    print("2. Обновление номера телефона")
    print("3. Удаление контакта")
    print("4. Выход")
    
    choice = input("Выберите действие (1-4):\n \n")

    if choice == '1':
        print_phonedirectory()
    elif choice == '2':
        name = input("Введите имя контакта для обновления номера: ")
        new_phone = input("Введите новый номер телефона: ")
        update_contact(name, new_phone)
    elif choice == '3':
        name = input("Введите имя контакта, которого хотите удалить: ")
        delete_contact(name)
    elif choice == '4':
        break
    else:
        print("Такого действия не существует! Выберите действие (1-4): ")