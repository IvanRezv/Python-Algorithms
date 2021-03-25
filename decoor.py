import time


def benchmark(func):
     def my_func():
         ts = time.time()
         # print('Code before function...')
         func()
         print(time.time() - ts)
         # print('Code after function...')
     return my_func

def count(func):
    """
    Декоратор - счётчик
    """

    counters = {}
    
    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)
    
    return wrapper

def logthis(func):
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__,args,kwargs)       
        return res
    return wrapped


@logthis
@count
@benchmark
def test():
    pass

test()
test()