# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [True, False]
y = [True, False]
z = [True, False]

itog = 0
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            if (not(x[i] or y[j] or z[k])) == (not x[i] and not y[j] and not z[k]):
                print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')
            else:
                itog = 1
                print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - False')
            
if itog == 0:
    print (f'Выражение - истинно')
else:
    print (f'Выражение - не истинно')
