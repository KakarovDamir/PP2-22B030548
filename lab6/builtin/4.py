import time 
start = time.time()
from math import *

n = int(input())

x = sqrt(n)
end = time.time()

print(f'Square root of {n} after {int(round((end-start),3)*1000)} miliseconds is {x}')
