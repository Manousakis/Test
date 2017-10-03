# coding=utf-8
from Folder.test2 import mySqrt

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    paramter = "hello!"

    def length(self):
        return mySqrt(self.x ** 2 + self.y ** 2)

    def show(self):
        return (self.x, self.y)

myvec = Vector(3,4)
print myvec.length()
print myvec.paramter
print myvec.show()
