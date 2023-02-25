def f(n):
    i = 0
    while i <= n:
        if i % 3 == 0 and i % 4 == 0 and i != 0:
            yield i
        i += 1

n = int(input())

for x in f(n):
    print(x, end = " ")