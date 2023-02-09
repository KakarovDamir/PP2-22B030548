def func(list1):
    list2 = []
    for x in list1:
        if x not in list2:
            list2.append(x)
    return list2
list1 = list(input().split())
print(func(list1))