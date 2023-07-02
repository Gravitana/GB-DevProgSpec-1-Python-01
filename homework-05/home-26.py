"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""


def multiplication(a1, b1, result1):
    if b1 < 2:
        return result1
    else:
        return multiplication(a1, b1 - 1, a1 * result1)


a = int(input('Введите число: '))
b = int(input('Введите показатель степени: '))

result = multiplication(a, b, a)

print(f'{a} в степени {b} = {result}')

