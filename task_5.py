# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30.

num = int(input('Введите число: '))
if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 !=0:
    print('True')
else:
    print('False')