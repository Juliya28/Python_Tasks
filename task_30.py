# 30. Вычислить число c заданной точностью d
# Пример:
# при 𝑑 = 0.001,𝜋 = 3.141 10−1≤𝑑≤10−10

import math
from math import pi

n = pi
print('Число 𝜋 =', n, '\n')

n = 100
pi_calculation = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

print('Число 𝜋 =', pi_calculation, '\n')
