from math import sqrt


print("Можно найти НОД, НОК, или узнать простое ли это число")
print("Далее запустится цикл из которого можно выйти только введя слово - выход или написать что-то кроме условия")
print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
move= input()
while move != "выход":
    if move == "NOD":
        print("Введите два числа :")
        a = int(input())
        b = int(input())
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        print("Нод =", a+b)
        print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
        move= input()
    elif move == "NOK":
        print("Введите два числа :")
        a = int(input())
        b = int(input())
        cloud= a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        print("Нок =", cloud //(a+b))
        print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
        move= input()
    elif move =="SIMPLE":
        print("Введите число для проверки")
        n = int(input())
        if n < 2:
            print("False, Число должно быть больше 1")
            print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
            move= input()
        elif n == 2 or n == 3:
            print("Это простое число")
            print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
            move= input()
        d = 2
        while d <= sqrt(n):
            if n % d == 0:
                print("Это сложное число")
            else:
                print("Это простое число")
            d +=1
            print("Что ты хочешь узнать? Введи NOK, NOD  или SIMPLE")
            move= input()
    else:
        print("Не понятен ввод")
        quit()