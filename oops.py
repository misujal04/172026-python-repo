class Rect:
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    def param(self):
        return 2* self.l * self.b
obj=Rect (10,20)
obj.area()
