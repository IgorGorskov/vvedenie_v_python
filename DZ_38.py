# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def exp():
    with open('num_book.txt', 'a', encoding='utf-8') as f:
        print('экспорт файла:')
        name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        sure_name = input('Введите отчество: ')
        num = input('Введите номер: ')
        f.writelines(f'{name} {last_name} {num} {sure_name}\n')
        
def imp():
    with open('num_book.txt', 'r+', encoding='utf-8') as f:
        print('импорт файла:')
        find = input('Введите имя/фамилию/номер ')
        for i in f.readline().split('\n'):
            if find in i:
                print(i)

def imp_all():
    with open('num_book.txt', 'r+', encoding='utf-8') as f:
        print('вывод всей книги:')
        print(f.read())


def delete():
    with open('num_book.txt', 'r+', encoding='utf-8') as f:
        dl = input('Введите номер удаяемого контакта: ')
        lines = f.readlines()
        for i in range(len(lines)):
            if dl in lines[i]:
                lines[i] = lines[i].replace(lines[i], '')

def add():
    with open('num_book.txt', 'r+', encoding='utf-8') as f:
       r = input('Введите номер редактируемого контакта: ')
       lines = f.readlines()
       for i in range(len(lines)):
            if r in lines[i]:
                name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                sure_name = input('Введите отчество: ')
                num = input('Введите номер: ')
                lines[i] = lines[i].replace(lines[i], f'{name} {last_name} {num} {sure_name}\n')
operation = int(input('Нажмите 1 если хотете импортировать данные,\nнажмите 2 если хотите экспортировать данные,\nнажмите 3 если хотите импортировать все данные\n'))
if operation == 1:
    imp()
elif operation == 2:
    exp()
elif operation == 3:
    imp_all()
elif operation == 4:
    delete()
elif operation == 5:
    add()