# Python Supports Overriding 

class Animal():
    def sound(self):
        print("Animal Makes Sound")
        
class Cat(Animal):
    def sound(self):
        print("Cat Makes Sound - Meow")

class Dog(Animal):
    def sound(self):
        print("Dog Makes Sound - Woof")
        
class Cow(Animal):
    def sound(self):
        print("Cow Makes Sound - Mooo")
        
cow_obj = Cow()
cow_obj.sound()

dog_obj = Dog()
dog_obj.sound()