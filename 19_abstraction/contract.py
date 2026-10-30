# Abstract Class
from abc import ABC, abstractmethod 

# No Abstraction i.e Concrete Class 
class Laptop:
    
    # No Abstraction i.e Concrete Method
    def should_have_processor(self):
        print("We Can See Functionality")
        print("We Can See Functionality")
        print("We Can See Functionality")
        print("We Can See Functionality")
        print("We Can See Functionality")

        
# With Abstraction
# Abstract Class 
class Laptop(ABC):
    
    # Abstract Method
    @abstractmethod
    def should_have_processor(self):
        pass 
    
    @abstractmethod
    def should_have_ram(self):
        pass 
    

        
    
    
