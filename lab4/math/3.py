import math 

sides = int(input())
length = int(input())

area = sides * (length ** 2) / (4 * math.tan(math.pi / sides))
print("The area of the polygon is:", int(area))