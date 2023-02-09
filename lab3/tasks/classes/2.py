class shape:
    def __init__(self):
        self.area = 0

    def Area(self):
        print(self.area)

class square(shape):
    def __init__ (self, length):
        self.length = length
        
    def Area(self):
        self.area = self.length ** 2
        print(self.area)

length = int(input())
x = square(length)
x.Area()