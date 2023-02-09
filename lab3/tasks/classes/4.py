class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of point: ({self.x} ; {self.y})")
    
    def move(self):
        print("Write a new coordinates for point2: ")
        self.x2 = int(input())
        self.y2 = int(input())
    
    def dist(self):
        self.di = (((self.y**2) + (self.x ** 2)) ** 0.5) - (((self.y2**2) + (self.x2 ** 2)) ** 0.5)
        if self.di < 0:
            self.di *= -1
        print(f"distance between ({self.x};{self.y}) and ({self.x2};{self.y2}) = {self.di}")

x = Point(1,1)
x.show()
x.move()
x.dist()
