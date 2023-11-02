import os

# Показать контакты
def print_data():
    print('\n№пп | Фамилия | Имя | Отчество | Телефон | Адрес')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        print('')

# Запись контакта

def input_name():
    return input('Введите имя контакта: ').title()

def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите номер телефона контакта: ')

def input_address():
    return input('Введите адрес контакта: ').title()

def add_contact():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        tel_file = data.read()
        num = len(tel_file.split('\n'))

    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        surname = input_surname()
        name = input_name()
        patronymic = input_patronymic()
        phone = input_phone()
        address = input_address()
        data.write(f'{num} | {surname} | {name} | {patronymic} | {phone} | {address}\n')
        print(f'Добавлена запись : {num} | {surname} | {name} | {patronymic} | {phone} | {address}\n')

# Поиск контакта
def search_contact():
     
    search = input('Введите данные для поиска: ').title()
    print()

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().split('\n')
       
    check_cont = False
            
    print('\n№пп | Фамилия | Имя | Отчество | Телефон | Адрес')
    for lines in contacts_list:
        if search in lines:
            print(lines)
            check_cont = True

    if not check_cont:
        print('Такого контакта нет')

# Изменение контакта
def change_contact():
    print('\n№пп | Фамилия | Имя | Отчество | Телефон | Адрес')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
    index_change_data = int(input('Введите номер строки для редактирования: ')) - 1
    tel_book_lines = tel_book.split('\n')
    edit_tel_book_lines = tel_book_lines[index_change_data]
    elements = edit_tel_book_lines.split(' | ')
    print(elements)
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[2]
    if len(patronymic) == 0:
        patronymic = elements[3]
    if len(phone) == 0:
        phone = elements[4]
    if len(address) == 0:
        address = elements[5]

    edited_line = f'{num} | {surname} | {name} | {patronymic} | {phone} | {address}'
    tel_book_lines[index_change_data] = edited_line
    print(f'Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n')
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))

# Удаление контакта
def delete_contact():
    print('\n№пп | Фамилия | Имя | Отчество | Телефон | Адрес')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    tel_book_lines = tel_book.split('\n')
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_tel_book_lines}\n')

    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))

# Интерфейс справочника

def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    os.system('cls')
    while command != '0':
        print('Меню пользователя: \n'
            '1. Вывод данных на экран \n'
            '2. Добавить контакт \n'
            '3. Поиск контакта \n'
            '4. Изменение контакта \n'
            '5. Удаление контакта \n'
            '0. Выход \n')
        command = input('Выберите пункт меню: ')

        while command not in ('1', '2', '3', '4', '5', '0'):
            print('Не корректный ввод, поворите запрос')
            command = input('Выберите пункт меню: ')

        match command:
            case '1':
                print_data()
            case '2':
                add_contact()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '0':
                print('Завершение программы')
        print()

if __name__ == '__main__':
    interface()