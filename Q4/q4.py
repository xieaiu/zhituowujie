list0 = [3, 1, 2, 3, 4, 1, 2]

def function1():
    list1 = []
    for item in list0:
        if item not in list1:
            list1.append(item)
    return list1


def function2():
    i = 0
    while i < len(list0):
        j = i + 1
        while j < len(list0):
            if list0[i] == list0[j]:
                list0.pop(j)
            else:
                j += 1
        i += 1
    return list0

def function3():
    list2 = list(dict.fromkeys(list0))
    return list2



print(function1())
print(function2())
print(function3())