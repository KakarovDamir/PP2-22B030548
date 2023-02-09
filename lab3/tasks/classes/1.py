class Person:
    def __init__(self):
        
        self.firstname = ''
        self.lastname = ''

    def GetString(self):
        self.firstname = str(input())
        self.lastname = str(input())
        
    def PrintString(self):
        f = self.firstname.upper()
        l = self.lastname.upper()
        print(f, l)

x = Person()  
x.GetString()
x.PrintString()
