def f(N):
    i = 1
    while i ** 2 < N:
        yield i ** 2
        i += 1

N = int(input())
for x in f(N):
    print(x)
