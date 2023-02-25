def f(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input())
for x in f(n):
    if x == n or x == n-1:
        print(x)
    else:
        print(x, end =", ")