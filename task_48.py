# 48. Задать список из n чисел последовательности (1 + 1\n)^n и вывести на экран их сумму.

import os
os.system("cls")

n = int(input('Введите число, которое будет обозначать длину списка: \n'))
massive = [1+(1/i)**i for i in range(1, n+1)]
print(massive, '\n')
print(f'{round(sum(massive), 3)}')
