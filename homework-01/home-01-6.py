"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""


def get_sum(number):
    s = 0

    for n in number:
        s += int(n)

    return s


not_correct = True

while not_correct:
    n = input('Введите шестизначный номер билета: ')

    if not n.isnumeric():
        print('Введённое значение не является числом!')
    elif len(n) != 6:
        print('Число не является шестизначным!')
    else:
        not_correct = False

s1 = get_sum(n[:3])
s2 = get_sum(n[3:])

print('-------------------------------')

if s1 == s2:
    print('Ура! Попался счастливый билет!')
else:
    print('Может повезёт в следующий раз?')