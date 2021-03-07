print("Какой длины будет диапазон?")
n = int(input())
print("Какую цифру нужно считать?")
d = int(input())
print("Далее вводите цифры по очереди")
count= 0
for i in range(1, n + 1):
    m = int(input("Число"+ str(i)+ ": "))
    while m > 0:
        if m % 10 == d:
            count +=1
        m = m // 10
print("Цифра-",d,"Встретилась ", count, "раз")