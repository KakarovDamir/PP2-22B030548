from math import *

def squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1

a = int(input())
b = int(input())
d = a
for x in squares(a,b):
    if d ** 2 == x:
        print(x, end = ' ')
    d += 1
    
