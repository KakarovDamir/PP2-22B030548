def f(n):
    while n > 0:
        yield n
        n -= 1

for x in f(10):
    print (x, end = ' ')