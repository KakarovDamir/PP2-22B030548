def isprime(num):
    for i in range(2,num//2 + 1):
        if num % i == 0:
            return False
    return True
l = list(map(int,input().split()))
filt = lambda l : filter(isprime,l)
print(list(filt(l)))