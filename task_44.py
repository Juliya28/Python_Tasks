# 44. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


n = int(input('Введите количество членов последовательности: \n'))
print('--------------------')

example = [3**x if x % 2 == 0 else (-3)**x for x in range(n)] # первый вариант
print(example)


example = [x for x in range(n)]
example = list(map(lambda x: 3**x if x % 2 == 0 else (-3)**x , example)) # второй вариант
print(example)