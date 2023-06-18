"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что
Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

not_correct = True

while not_correct:
    s = input('Введите общее количество журавликов: ')

    if not s.isnumeric():
        print('Введённое значение не является числом!')
    elif int(s) % 6 > 0:
        print('Количество журавликов должно быть кратно шести!')
    else:
        not_correct = False

s = int(s)
petya_sereza = round(s / 6)
katya = round(petya_sereza * 4)

print(f'Катя сделала {katya} журавликов, а Петя с Серёжей по {petya_sereza} каждый')
