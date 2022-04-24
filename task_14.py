# 14.	Подсчитать сумму цифр в вещественном числе.

# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

a = random.uniform(1, 101)
print('\n Задано число:', a)

a = str(a).replace('.', '')     
# print(a)
summa = sum(map(int, a))        
print('\n Сумма цифр данного числа равна:', summa, '\n')
