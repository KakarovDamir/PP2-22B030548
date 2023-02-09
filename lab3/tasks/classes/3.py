class shape:
    def __init__(self, area):
        self.area = area

    def Area(self):
        print(self.area)

class Rectangle(shape):
    def __init__(self,area,length,width):
        super().__init__(area)
        self.length = length
        self.width = width

    def find(self):
        self.area = self.width * self.length
        print(self.area)

a = 0
length = int(input())
width = int(input())
rec = Rectangle(a,length,width)

rec.find()
