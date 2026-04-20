#import math
from math import sqrt
bad_data = True
while bad_data == True:

    try:
        a = int(input('Введите число a : '))
        b = int(input('Введите число b : '))
        c = int(input('Введите число c : '))

        bad_data = False

    except:
        print('Вы ввели некорректные данные!!!')

D = b * b - (4 * a * c)
print(f'Так, как дискриминант = {D}')

if D < 0:
    print('Уравнение не имеет корней')
elif D == 0:
    x1 = (-b) / (2*a)
    print(f'Уравнение имеет один корень X1 = {x1}')
else:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - sqrt(D)) / (2 * a)

    print(f'Это уравнение имеет два корня: \n X1 = {x1}  \n X2 = {x2}')