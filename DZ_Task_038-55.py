"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных."""

phonebook = {}

def add_contact(name, phone):
    """Добавление контакта в телефонную книгу"""
    phonebook[name] = phone
    print(f"Контакт {name} добавлен в телефонную книгу с номером {phone}.")

def update_contact(name, new_phone):
    """Обновление номера телефона для существующего контакта"""
    if name in phonebook:
        phonebook[name] = new_phone
        print(f"Номер телефона для {name} обновлен: {new_phone}.")
    else:
        print(f"{name} не найден в телефонной книге.")

def delete_contact(name):
    """Удаление контакта из телефонной книги"""
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} удален из телефонной книги.")
    else:
        print(f"{name} не найден в телефонной книге.")

def print_phonebook():
    """Печать содержимого телефонной книги"""
    if phonebook:
        print("Телефонная книга:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Телефонная книга пуста.")

# Пример использования функций:
add_contact("Иван Иванов", "123-456-789")
add_contact("Петр Петров", "987-654-321")

print_phonebook()

update_contact("Иван Иванов", "111-222-333")
delete_contact("Петр Петров")

print_phonebook()