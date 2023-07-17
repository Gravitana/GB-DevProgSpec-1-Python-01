"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

from database import *
from view import *

def main():
    while True:
        print_alert("\nВыберите действие:\n1 - Новая запись\n2 - Найти запись\n3 - Сортировка по имени\n4 - Редактировать запись\n5 - Вывести все записи\n0 - Завершить работу")
        num = input_num()
        if num == 0:
            break
        elif num == 1:
            row = str(get_new_id()) + ";" + input_data("Введите имя: ") + ";" + input_data("Введите номер телефона: ")
            write_one_row(row)
            print_alert("Запись сохранена")
        elif num == 2:
            char = input_char()
            rows = search_data(char)
            if rows:
                print_alert("Найдено:")
                for row in rows:
                    print_row_data(row.split(';'))
            else:
                print_alert("Ничего не найдено")
        elif num == 3:
            lst = get_all()
            lst.sort(reverse=False, key=lambda r: r.split(';')[1])
            print_all_data(lst)
        elif num == 4:
            ask_edit_data()
        elif num == 5:
            print_all_data(get_all())
    print_alert("Программа завершена")

def ask_edit_data():
    print_all_data(get_all())
    print_alert('Введите id записи для редактирования или "0" для отмены')
    row_id = input_num()
    if row_id > 0:
        ask_edit_row(row_id)

def ask_edit_row(row_id):
    while True:
        lst = get_all()
        row = get_row_by_id(row_id, lst)
        if not row:
            print_alert("Ничего не найдено")
            break
        print_alert("\nВыберите действие:\n1 - Редактировать имя\n2 - Редактировать телефон\n3 - Удалить запись\n0 - Выйти из редактирования")
        num = input_num()
        if num == 0 or num > 3:
            break
        elif num == 3:
            delete_row(row)
            print_alert("Запись удалена")
            print_all_data(lst)
            break
        else:
            key = lst.index(row)
            data = row.split(';')
            if num == 1:
                data[1] = input_data("Введите имя: ")
            elif num == 2:
                data[2] = input_data("Введите номер телефона: ")
            row = ';'.join(data)
            lst[key] = row
            overwrite_all_data(lst)
            print_alert("Запись обновлена")
            print_row_data(data)

def print_all_data(lst):
    if lst:
        for row in lst:
            print_row_data(row.split(';'))
    else:
        print_alert("Ничего не найдено")

init_db()
main()
