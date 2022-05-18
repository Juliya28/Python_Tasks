# 47. Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 6, 24]

import os
os.system("cls")
from itertools import accumulate
import operator

n = int(input('Введите число, которое будет обозначать длину списка: '))

li = list(accumulate([x for x in range(1, n + 1)], operator.mul))
print('\n', li, '\n')
