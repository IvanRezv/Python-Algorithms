import math
import cmath
print("Введите по очереди a,b и c (учтите то , что а не может быть равно 0)")
a= input()
b= input()
c= input()
a= float(a)
b= float(b)
c= float(c)
if a == 0:
    print("a не может быть равно 0")
else:
    print("Вы ввели =", a , b, c)
    discriminant= pow(b,2) - 4*a*c
    print("Дискриминант=",discriminant)
    if discriminant == 0:
        x = -b / (2*a)
        print("Корень= ",x)
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print("Первый корень = ", x1)
        print("Второй корень = ", x2)