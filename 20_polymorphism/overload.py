# Python Doesn't Support Overloading 

class Maths:
    
    def add(self,a,b):
        return a + b 
    
    def add(self,a,b,c):
        return a + b + b 
    
obj = Maths()
obj.add(2,3)
obj.add(2,3,4)