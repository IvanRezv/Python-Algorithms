def bank (a, years,procent):

    for i in range (years):

        a = a + (a/100*procent)

    return (a)

result = bank (float(input("Введите сумму вклада: ")), int(input("На сколько лет: ")),int(input("Введите процент: ")))

print (result)