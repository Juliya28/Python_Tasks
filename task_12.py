# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")

Dictionary = {}
n = int(input('Введите значение n: '))
for i in range(1,n+1):
    Dictionary[i] = 3*i+1
print(f'\n {Dictionary} \n')
