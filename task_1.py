# 1. По двум заданным числам проверить является ли одно квадратом второго.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a == b**2 or b == a**2:
    print('Одно из чисел является квадратом другого!')
else:
    print('Число не является квадратом другого!')