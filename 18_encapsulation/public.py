# Public Access - Can Access Anywhere 

class A:
    def __init__(self,a):
        self.a = a # Public i.e Without any special naming conventions or prefixes 
        
obj = A(10)

print(obj.a) # Outside We Can Access A 