def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for x in range(0, last_item):
            print("Сдвиг",mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist


user_input = input("Введите список элементов, в формате - 1,2,3: ")
oldlist = list(map(float, user_input.split(',')))

print("Ваш старый введенный массив: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("Отсортированный пузырем массив: ", newlist)