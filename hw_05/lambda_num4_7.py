"""
Номер 4 и 7

рекурсия
"""
factrec = lambda x: 1 if x == 0 else x * factrec(x-1)

print(factrec(4))

"""
не рекурсия
"""

def recursive_lambda(func):
    def ret(*args):
        return func(ret, *args)
    return ret
n=int(input("Введите значение для которого найти факториал: "))
print(recursive_lambda(lambda factorial, x: x * factorial(x - 1) if x > 1 else 1)(n))