def histogram(list1):
    for x in list1:
        for i in range(int(x)):
            print('*', end = "")
        print()
list1 = list(input().split())
histogram(list1)