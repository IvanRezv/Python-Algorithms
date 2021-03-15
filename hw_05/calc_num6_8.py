from math import pow

def calc(a=1, b=2, operation="+"):
    def add(a1, b1):
        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        return a1 / b1

    def power(a1,b1):
        return pow(a1,b1)


    selector = {
        "+": add,
        "-": remove,
        "*": multiply,
        "/": divide,
        "^": power
        }

    return selector[operation](a, b)

print("Ты запустил калькулятор, если хочешь из него выйти нажми пробел на стадии выполнения операций")
print('Введите два числа:')
x=input('Число 1 -')
y=input("Число 2- ")
try:
    x=float(x)
    y=float(y)
except (ValueError, AttributeError):
    print("Ты ввёл не число, извинись и начни заного")
    quit()


print("Выбери, что хочешь сделать - + - * / ^ ")

ops=input()

while ops != ' ':
    if ops == '+':
        print(calc(x, y, '+'))
        print("Выбери, что хочешь сделать - + - * / ^ ")
        ops=input()
    elif ops == '-':
        print(calc(x, y, '-'))
        print("Выбери, что хочешь сделать - + - * / ^ ")
        ops=input()
    elif ops == '*':
        print(calc(x, y, '*'))
        print("Выбери, что хочешь сделать - + - * / ^ ")
        ops=input()
    elif ops == '/':
        try:
            print(calc(x, y, '/'))
            print("Выбери, что хочешь сделать - + - * / ^ ")
            ops=input()
        except ZeroDivisionError:
            print ("Деление на ноль,запускай заного")
            quit()
    elif ops == '^':
        print(calc(x, y, '^'))
        print("Выбери, что хочешь сделать - + - * / ^ ")
        ops=input()
    else:
        ops = input("Не понял тебя, вводи заного ")


"""
print(calc(x, y, '+'))
print(calc(x, y, '-'))
print(calc(x, y, '*'))
print(calc(x, y, '/'))
print(calc(x, y, '^'))
"""