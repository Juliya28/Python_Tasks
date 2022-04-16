# 2. Найти максимальное из пяти чисел.

numbers = range(1, 6)
max = 0
for i in numbers:
    if i > max:
        max = i
        print(i, end=' ')
print()
print('Максимальное число: ', max)


