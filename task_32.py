# 32. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

def list(size, m, n):
    return [randint(m, n) for i in range(size)]

def unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = list(size, m, n)
print(origin, '\n')
print(unic_value(origin), '\n')