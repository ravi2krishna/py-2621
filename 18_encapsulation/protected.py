# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e With __ prefixes 

class B(A):
    def showA(self):
        a = A(10)
        print(a.__a) # Access Parent Data In Sub class         

objB = B(20)
# objB.showA()

# Protected Access 
class A:
    def __init__(self,a):
        self._a = a # Protected i.e With _ prefixes 

class B(A):
    def showA(self):
        a = A(10)
        print(a._a) # Access Parent Data In Sub class         

objB = B(20)
objB.showA()