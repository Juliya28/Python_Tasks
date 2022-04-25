# 18. Реализовать алгоритм перемешивания списка. 

import os
import random
os.system("cls")

# list = [random.randint(1, 101) for item in range(10)]
list = [1, 6, 5, 89, 45, 24, 56]
print(list, '\n')
random.shuffle(list)
print(list, '\n')
