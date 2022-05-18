# 49. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите значение для крайних точек: '))

data = open('task_49.txt', 'r')


elements = [i for i in range (-n, n + 1)]
print(elements, '\n')

elements_file = [int(line.strip()) for line in data]
print(elements_file, '\n')

list1 = [x * y for x, y in zip(elements_file, elements)]
print(list1, '\n')
data.close() 
