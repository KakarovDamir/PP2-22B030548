def filter_prime(mylist):
    list2 = []
    for x in mylist:
        n = b = int(x)
        cnt = 0
        for i in range(1,n+1):
            if b == 1:
                list2.append(b)
            if b % i == 0:
                cnt += 1
            else:
                continue
        if cnt == 2:
            list2.append(b)
        else:
            continue
    print(list2)

mylist = list(input().split())
filter_prime(mylist)
