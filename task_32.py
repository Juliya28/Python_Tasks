# 32. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

def list(size, m, n):
    return [randint(m, n) for i in range(size)]

def value(list):
    return [i for i in set(list)]

size = int(input('Введите число, которое будет обозначать количество элементов списка: '))
m = 1
n = 10

origin = list(size, m, n)
print(origin, '\n')
print(value(origin), '\n')