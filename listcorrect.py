print("Введите последовательность без пробела")
a=input("Введите последовательность= ")
a = list(set(a))
print("Список без дублей: ", a)
"""
Пузырек для сортировки
"""
def bubble_list(a):
    n = len(a)
    for j in range(0, n -1):
        for i in range(0,n-j-1):
            if a[i] < a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    return a

bubble_list(a)
print("Список отсортированный по убыванию:",a)

