# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти.

number = input('Введите номер четверти от 1 до 4: ')
print()

while not(number.isnumeric()):
    number = input(f'Ввели не правильное значение {number}!\n')
else:
    number = abs(int(number))
    if number > 4:
        print(f'Ввели не правильное значение {number}!\n')
    elif number == 1:
        print(f'Допустимые значения координат - (x > 0 и y > 0) для четверти: {number}!\n')
    elif number == 2:
        print(f'Допустимые значения координат - (x < 0 и y > 0) для четверти: {number}!\n')
    elif number == 3:
        print(f'Допустимые значения координат - (x < 0 и y < 0) для четверти: {number}!\n')
    elif number == 4:
        print(f'Допустимые значения координат - (x > 0 и y < 0) для четверти: {number}!\n')
