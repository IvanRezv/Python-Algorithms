def search(mylist, target, smallest, biggest):
    if smallest > biggest:
        return False
    else:
        midle = (smallest + biggest) // 2
        if target == mylist[midle]:
            return midle
        elif target < mylist[midle]:
            return search(mylist, target, smallest, midle - 1)
        else:
            return search(mylist, target, midle + 1, biggest)


user_input = input("Введите список элементов, в формате - 1,2,3: ")
list = list(map(float, user_input.split(',')))
target = float(input("Введите число из списка, индекс которого вам нужен:"))
smallest = 0
biggest = len(list)

x = search(list, target, smallest, biggest)

if not x:
    print("Item", target, "Not found")
else:
    print("Item", target, "Found at Index", x)
