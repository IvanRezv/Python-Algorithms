mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]


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


mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
target = 1
smallest = 0
biggest = len(mylist)

x = search(mylist, target, smallest, biggest)

if not x:
    print("Item", target, "Not found")
else:
    print("Item", target, "Found at Index", x)
