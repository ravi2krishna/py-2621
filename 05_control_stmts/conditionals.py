# Conditional Structures (Decision Making Statements)

# if 

if True: # When True Execute 
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
print("===================")


if False: # Code is not analyzed because condition is statically evaluated as false 
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
# if condition with dynamic 
if 5 > 2:
    print("Yes 5 > 2 Is Correct")
    
if 5 < 2:
    print("Yes 5 < 2 Is Correct") 
    
num = 10
if num > 0:
    print("Given Num Is Positive")
if num < 10:
    print("Given Num Is Negative")
    
num = -10
if num > 0:
    print("Given Num Is Positive")
if num < 10:
    print("Given Num Is Negative")
    
print("===================")

# if else 
num = -10
if num > 0: # if condition is true
    print("Given Num Is Positive")
else: # if condition is false
    print("Given Num Is Negative")
    
print("===================")

# Without input() data is hardcoded / fixed 
name = "Ravi" # this is fixed i.e static 
print(name)

# With input() data is dynamic 
name = input("Enter Your Name: ")
print(name)

print("===================")

username = input("Enter Your Username: ")
print(username)
print("Welcome: "+username) # + Operator Concatenation 
print("Welcome: ",username) # , Operator 
print("Welcome: {username}") # , No Interpolation 
print(f"Welcome: {username}") # , With Interpolation 

print("===================")

num = input("Enter Your Number: ")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"Given Num {num} Is Positive")
else: 
    print(f"Given Num {num} Is Negative")
    
print("===================")

# Voting Application Dynamic 
# age = input("Enter Your Age: ")
# age = int(age)
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")