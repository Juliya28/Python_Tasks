# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_of_prime_factors(n):
    list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
    return list

z = int(input('Введите число: '))
print(list_of_prime_factors(z), '\n')
