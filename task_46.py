# 46. Подсчитать сумму цифр в вещественном числе.

import os
import random
os.system("cls")

num = round(random.uniform(1, 101), 10)
print('\n Рандомно заданое число:', num)

num = str(num).replace('.', '')     
summa = sum(map(int, num))        
print('\n Сумма цифр данного числа равна:', summa, '\n')