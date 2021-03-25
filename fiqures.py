from operations import *

class Cube(Square):
    def area(self,side):
        return 6 * (side*side)
    def bulk(self,side):
        return side * side * side

class Paralellipiped(Pryamougolnik):
    def bulk(self,side_a,side_b,height):
        return side_a * side_b * height

class ball(Ellipse):
    def bulk(self,radius):
        return (4*pi*pow(radius,3))/3


while True:
    string = input("""
    Какая фигура вас интересует?
    1.Квадрат
    2.Ромб
    3.Треугольник
    4.Прямоугольник
    5.Эллипс
    """)

    if string == "1":
        move= input("""
        Выберете действие:
        1.Площадь
        2.Периметр
        3.Объем
        """)
        if move == "1":
            kv=Square()
            a = float(input("Введи сторону= "))
            print(kv.area(a))
        elif move == "2":
            kv=Square()
            a = float(input("Введи сторону= "))
            print(kv.perimetr(a))
        elif move == "3":
            print("Квадрат без объема, могу предложить вам для куба посчитать?")
            kub=Cube()
            a = float(input("Введи сторону куба = "))
            print("Площадь его= ",kub.area(a),"И объем =",kub.bulk(a))
    
    if string == "2":
        move= input("""
        Выберете действие:
        1.Площадь
        2.Периметр
        3.Объем
        """)
        if move == "1":
            rom=Romb()
            a = float(input("Введи длину стороны="))
            b = float(input("Введи длину высоты="))
            print(rom.area(a,b))
        elif move == "2":
            rom=Romb()
            a = float(input("Введи длину стороны="))
            print(rom.perimetr(a))
        elif move == "3":
            print("Не могу посчитать объем для ромба")

    if string == "3":
        move= input("""
        Выберете действие:
        1.Площадь
        2.Периметр
        3.Объем
        """)
        if move == "1":
            rect=Rectangle()
            a = float(input("Введи сторону="))
            b = float(input("Введи высоту="))
            print(rect.area(a,b))
        elif move == "2":
            rect=Rectangle()
            a,b,c = float(input("Первая сторона=")),float(input("Вторая сторона=")),float(input("Третья сторона="))
            print(rect.perimetr(a,b,c))
        elif move == "3":
            print("Не могу посчитать объем для треугольника")

    if string == "4":
        move= input("""
        Выберете действие:
        1.Площадь
        2.Периметр
        3.Объем
        """)
        if move == "1":
            pryam=Pryamougolnik()
            a = float(input("Введи длину="))
            b = float(input("Введи ширину="))
            print(pryam.area(a,b))
        elif move == "2":
            pryam=Pryamougolnik()
            a = float(input("Введи длину="))
            b = float(input("Введи ширину="))
            print(pryam.perimetr(a,b))
        elif move == "3":
            print("Не могу посчитать объем для прямоугольника, но могу для прямоугольного параллелипипеда")
            pryam = Paralellipiped()
            a = float(input("Введи длину="))
            b = float(input("Введи ширину="))
            c= float(input("Введи высоту="))
            print(pryam.bulk(a,b,c))

    if string == "5":
        move= input("""
        Выберете действие:
        1.Площадь
        2.Периметр
        3.Объем
        """)
        if move == "1":
            el=Ellipse()
            a = float(input("Введи длину большой полуоси="))
            b = float(input("Введи длину малой полуоси="))
            print("Приблизительно равен=",el.area(a,b))
        elif move == "2":
            el=Ellipse()
            a = float(input("Введи длину большой полуоси="))
            b = float(input("Введи длину малой полуоси="))
            print("Приблизительно равен=",el.perimetr(a,b))
        elif move == "3":
            print("Не могу посчитать объем для эллипса, но могу для шара")
            myach= ball()
            rad=float(input("Введи радиус шара="))
            print("Приблизительно равен= ",myach.bulk(rad))
    
    print('Повторим?')
    print('1: Да')
    print('2: Нет')
    vop = int(input())
    if vop == 1:
        continue
    elif vop == 2:
        print('')
        break