# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e With __ prefixes 
        
obj = A(10)

print(obj.a) # AttributeError: 'A' object has no attribute 'a'

# Real World Use Case
class CreditCardPayment:
    def __init__(self,card_number,card_cvv):
        # self.card_number = card_number # This is Public (No Encapsulation)
        self.__card_number = card_number # Recommended i.e Private 
        self.__card_cvv = card_cvv # Recommended i.e Private 