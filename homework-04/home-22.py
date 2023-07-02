"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


n = int(input('Введите количество элементов в первом массиве: '))
m = int(input('Введите количество элементов во втором массиве: '))

list_n = []
list_m = []

for i in range(n):
    n_i = int(input(f'Введите {i}-й элемент первого массива: '))
    list_n.append(n_i)

print('Первый массив заполнен')

for i in range(m):
    m_i = int(input(f'Введите {i}-й элемент второго массива: '))
    list_m.append(m_i)

print('Второй массив заполнен')

print(list_n)
print(list_m)

set_n = set(list_n)
set_m = set(list_m)

set_r = set_n.intersection(set_m)

print('----------------------------------------')
print('Общие элементы:')
print(quicksort(list(set_r)))
