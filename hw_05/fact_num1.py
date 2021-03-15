def fact():
    while True:
        try:
            n=int(input("Введите число ") )
        except:
            print("Это не число, давай ещё раз ")
            continue
        else:
            fact = 1
            while n > 1:
                fact *= n
                n -= 1
            print("Факториал этого числа: ",fact)
            break

fact()
