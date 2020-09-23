import math, cmath;
print('ИУ5-43 Гаврилов Леонид')
l = []
i = 0
while i < 3:
    try:
        print('Введите коэффициенты: ')
        l.append(int(input()))
        i = i + 1
    except ValueError:
        print('Коэффициент А, В или С введен некорректно. Пожалуйста повторите.')
a, b, c = l
print('Вы ввели ', int(a), 'x^4 +', int(b), 'x^2 +', int(c), '= 0')
D = b*b - 4 * a * c
print("Дискриминант:",D)
if D > 0:
    t1 = (-b + math.sqrt(D)) / (2 * a)
    t2 = (-b - math.sqrt(D)) / (2 * a)
    x1 = cmath.sqrt(t1)
    x2 = -cmath.sqrt(t1)
    x3 = cmath.sqrt(t2)
    x4 = -cmath.sqrt(t2)
    print("Всего 4 корня",x1,x2,x3,x4)
elif D == 0:
    t = (-b) / 2 * a
    x1 = cmath.sqrt(t)
    x2 = -cmath.sqrt(t)
    print("Всего 2 корня",x1, x2)
else:
    print('Нет корней')