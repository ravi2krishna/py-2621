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

print("===================")
    
# Conditional Expression 
age = int(input("Enter Your Age: "))
# value_if_true if condition else value_if_false 
print("You Can Vote" if age >= 18 else "You Cannot Vote")

print("===================")

# Say I Want To Check If Student Passed Or Failed 
marks = int(input("Enter Your Marks: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED")
    
print("===================")

# Say I Want To Check For Grades
# elif ladder
# 90 and above - A Grade
# 75 and above but below 90 - B Grade
# 60 and above but below 75 - C Grade
# 60 and above but below 50 - D Grade
# 35 and above but below 50 - E Grade
# Below 35 Failed 
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("FAILED")
    
print("===================") 

# match case 
error_code = int(input("Enter Error Code You Are Seeing: "))
match error_code:
    case 200:
        print("Success - OK")
    case 404:
        print("Error Page Not Found")
    case 500:
        print("Error Server Not Responding")
    case _:
        print("Unknown Error Code")
 
print("===================") 
  
# match case 
user_role = input("Enter Your User Role: ")
match user_role:
    case "admin":
        print("Full Access")
    case "student":
        print("Read Only Access")
    case "trainer":
        print("Read & Write Access")            
    case _:
        print("Unknown User Role")

print("===================") 