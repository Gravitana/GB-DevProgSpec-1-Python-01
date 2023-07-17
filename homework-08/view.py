def input_num():
    return int(input())

def input_data(alert):
    return input(alert)

def input_char():
    char = input("Введите характеристику: ")
    return char

def print_row_data(row_data):
    print('{}) {} – {}'.format(row_data[0], row_data[1], row_data[2], ), end='')

def print_alert(alert):
    print(alert)
