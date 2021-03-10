def bubble_list(nums):
    n = len(nums)
    for j in range(0, n -1):
        for i in range(0,n-j-1):
            if nums[i] < nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums

"""
Далее функция для рандомного массива
"""
from random import randint

def bubble_random_array(array):
    for i in range(k-1):
        for j in range(k-i-1):
            if array[j] > array[j+1]:
                house= array[j]
                array[j]= array[j+1]
                array[j+1]= house

"""
Вызовы функция для массива и для списка
Только у меня для списка в обратном порядке после сортировки стоят, но суть я думаю передал
"""
k=4
a=[]
for i in range(k):
    a.append(randint(1,99))

print(a)
bubble_random_array(a)
print(a)



random_list = [1, 2, 3, 4]
print(random_list)
bubble_list(random_list)
print(random_list)

abra = [2192, 123, 123, 12321]
print(abra)
bubble_list(abra)
print(abra)