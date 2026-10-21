# Inbuilt Modules 

# def sqrt():
#     print("Giving Square Root")
    
# sqrt()

# sqrt() # NameError: name 'sqrt' is not defined

# 1st Syntax 
# print(math.sqrt(25)) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print(math.sqrt(25))
print(math.pi)
print(math.e)

print("=" * 20)

# 2nd Syntax 
# from module import specific_functionality # Recommended
# from math import pi
# print(pi)
# print(e) # NameError: name 'e' is not defined

from math import pi,e
print(pi)
print(e) 