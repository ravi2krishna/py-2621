# Functional Programming 

# Without Functions 

# User One Wants To Calculate Mathematical Operations For Below Values
num1 = 10
num2 = 5 

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Two Wants To Calculate Mathematical Operations For Below Values
num1 = 20
num2 = 10 

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Three Wants To Calculate Mathematical Operations For Below Values
num1 = 30
num2 = 10 

# Math Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)    

# User One Wants To Calculate Mathematical Operations For Below Values
num1 = 10
num2 = 5 
math_ops() 
print("=" * 50)
# User Two Wants To Calculate Mathematical Operations For Below Values
num1 = 20
num2 = 10 
math_ops() 
print("=" * 50)
# User Three Wants To Calculate Mathematical Operations For Below Values
num1 = 30
num2 = 10 
math_ops() 
print("=" * 50)

# With Parameters 
# math_ops(1,2) # TypeError: math_ops() takes 0 positional arguments but 2 were given
def math_ops(num1,num2): # num1 and num2 are parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2) 

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'

# User One Wants To Calculate Mathematical Operations For Below Values
math_ops(10,5) # 10, 5 are arguments 
print("=" * 50)  
math_ops(20,10) 
print("=" * 50)  
math_ops(30,10) 
print("=" * 50)  

# processes data
def process_email(email_id):
    print(email_id.lower()+"@gmail.com")
    
process_email("RaVI2KRisHNa")
print("=" * 50) 
process_email("JOhN_dOE")
print("=" * 50) 

# Positional Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi@gmail.com")   

print("=" * 50)  

employee_info("Ravi","ravi@gmail.com","Hyderabad")   

print("=" * 50)  

# Keyword Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi@gmail.com")   

print("=" * 50) 

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")   

print("=" * 50) 

# Without Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",org_name="IBM")   

print("=" * 50) 

employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com",org_name="IBM")   

print("=" * 50) 

employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com",org_name="IBM")   

print("=" * 50) 


# With Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name="IBM"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")   

print("=" * 50) 

employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com")   

print("=" * 50) 

employee_info(emp_location="Bangalore",emp_name="Mike",emp_email="mike@gmail.com")   

print("=" * 50) 

employee_info(emp_location="New York",emp_name="Ross",emp_email="ross@gmail.com",org_name="ORACLE")   

print("=" * 50) 

# With Default Arguments and Placement Requirement
# def employee_info(emp_name,emp_email,emp_location,org_name="IBM",emp_mobile): 
#     # Non-default argument follows default argument
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")   

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="IBM",gst="9876789876"): 
    # Non-default argument follows default argument
    print(f"Hi {emp_name} your email is {emp_email}, mobile number is {emp_mobile} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",emp_mobile=999999)  

print("=" * 50) 

# Without Arbitrary Positional Arguments 
def add_numbers(n1):
    print(n1)
    
def add_two_numbers(n1,n2):
    print(n1+n2)
    
def add_five_numbers(n1,n2,n3,n4,n5):
    print(n1+n2+n3+n4+n5)
    
add_numbers(1)
print("=" * 50) 
add_two_numbers(1,2)
print("=" * 50) 
add_five_numbers(1,2,3,4,5)
print("=" * 50) 


# With Arbitrary Positional Arguments 
def add_numbers(*numbers):
    print(numbers)

add_numbers(10)
print("=" * 50)
add_numbers(10,20)
print("=" * 50)
add_numbers(10,20,30,40,50)
print("=" * 50)

# With Arbitrary Positional Arguments 
def add_numbers(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num 
    print(f"Total Sum is {total_sum}")

add_numbers(10)
print("=" * 50)
add_numbers(10,20)
print("=" * 50)
add_numbers(10,20,30,40,50)
print("=" * 50)

def profile(*info):
    print(info)
    
profile("ravi")
print("=" * 50)
profile("ravi",90909090,9.5,True)
print("=" * 50)

# Real World Use Case is Ecommerce Cart 
def cart_total_value(*products):
    total_cart = 0
    for price_product in products:
        total_cart += price_product 
    print(f"Total Sum is {total_cart}")

# Customer One    
cart_total_value(1099,185,595)
print("=" * 50)

# Customer Two    
cart_total_value(1299,1085,1595,1800)
print("=" * 50)

# Arbitrary Keyword Arguments 
def profile(**info):
    print(info)
    
profile(first_name="ravi")
print("=" * 50)
profile(first_name="ravi",mob_num=90909090,gpa=9.5,passed=True)
print("=" * 50)

def profile(**info):
    for data in info:
        print(data) # Key 
    
profile(first_name="ravi",mob_num=90909090,gpa=9.5,passed=True)
print("=" * 50)

def profile(**info):
    for data in info:
        print(info[data]) # Value 
    
profile(first_name="ravi",mob_num=90909090,gpa=9.5,passed=True)
print("=" * 50)

# Real World Use Case -> https://i.ytimg.com/vi/tfZOZWVb81M/hq720.jpg?sqp=-oaymwEYCJUDENAFSFryq4qpAwoIARUAAIhC0AEB&rs=AOn4CLD61RCES1Oo8OL919n3tkbqnBt2yA

# Real World Use Case -> jan=3000, feb=4500, mar=9000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000, may=3000, jun=5000

def bank_transactions(**transactions):
    print(transactions)
    total_transactions_value = 0
    total_transactions_count = 0
    for transaction in transactions:
        total_transactions_value += transactions[transaction]
        total_transactions_count += 1
    print(f"Total Transactions Amounts To {total_transactions_value} for {total_transactions_count} Transactions")
        

bank_transactions(jan=3000, feb=4500, mar=9000)
print("=" * 50)
bank_transactions(jan=3000, feb=4500, mar=9000, apr=6000, may=3000, jun=5000)
print("=" * 50)

# without return
def add(a,b):
    a + b 
    
add(10,20)
print(add(10,20))

print("=" * 50)

# with return
def add(a,b):
    return a + b 

print(add(10,20))

print("=" * 50)

# # Problem Statement 
# def add(a,b):
#     print(a+b) # None
    
# # function composition
# def sub(c,d,e): # add c & d, then minus e --> c + d - e 
#     print(add(c,d) - e) # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
    
# sub(3,4,5) # 3 + 4 - 5 = 2 (None - 5) 

# Problem Statement 
def add(a,b):
    return a+b # 7
    
# function composition
def sub(c,d,e): # add c & d, then minus e --> c + d - e 
    print(add(c,d) - e) 
    
sub(3,4,5) # 3 + 4 - 5 = 2 

print("=" * 50)

# If you use return, make sure it's the last part of statement to be executed   
def add(a,b):
    print("Calculation Started")
    return a+b 
    print("Calculation Completed") # Code is structurally unreachable

print(add(5,5))

print("=" * 50)

# If you have multiple return statements, first return will be considered 
a = 50
a = 60
a = 70

print(a)

print("=" * 50)

def math_ops(n1,n2):
    return n1 + n2
    return n1 - n2 # Code is structurally unreachable
    return n1 * n2 # Code is structurally unreachable

print(math_ops(1,2))

print("=" * 50)

def math_ops(n1,n2,operator):
    if operator == "+":
        return n1 + n2 
    elif operator == "-":
        return n1 - n2 
    elif operator == "*":
        return n1 * n2 
    elif operator == "/":
        return n1 / n2 
    else:
        return "Invalid Operator Given"
    
print(math_ops(10,5,"+"))

print("=" * 50)

print(math_ops(10,5,"*"))

print("=" * 50)

print(math_ops(10,5,"$"))

print("=" * 50)

# Local Scope 
def add():
    la = 10 # Local - inside the function
    lb = 20 # Local - inside the function
    # Accessing within function
    print(la)
    print(lb)
    
add()

# accessing outside the function
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

print("=" * 50)

# Parameters we pass to the functions, are also local variables 
def add(la,lb): # Local - inside the function    
    print(la)
    print(lb)
    
add(30,40)

# accessing outside the function
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

print("=" * 50)

# Global Scope 
ga = 100 # global - outside the function

def add(la,lb): # Local - inside the function    
    print(la)
    print(lb)
    print(ga) # global accessed inside the function
    
add(50,60)

print(ga) # global accessed outside the function

print("=" * 50)

# name conflicts
ga = 500 # global - outside the function

def add(la,lb,ga): # Local - inside the function    
    print(la)
    print(lb)
    print(ga) # local accessed inside the function
    print(globals()['ga']) # global access inside the function
    
add(70,80,90)

print("=" * 50)

# global variable outside the function
count = 0
print(count)
count += 1
print(count)

print("=" * 50)

# global variable inside the function
count = 0
print(count)

def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count

print(increment())

print("=" * 50)

# Without Lambda i.e Standard Functions 
def add(a,b):
    return a + b 

print(add(100,50))

print("=" * 50)

# With Lambda Functions 
# lambda arguments:expression 
lambda a,b:a+b
# print((lambda_function)(arguments)) # IILE 
print((lambda a,b:a+b)(4,5))

print("=" * 50)

# Without Lambda i.e Standard Functions
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 
    
print(is_even_num(11))

print("=" * 50)

print(is_even_num(10))

print("=" * 50)

# With Lambda Functions 
# lambda arguments:expression 
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0)(5)) 
print("=" * 50)
print((lambda num:num % 2 == 0)(7)) 
print("=" * 50)
print((lambda num:num % 2 == 0)(4)) 
print("=" * 50)

# Without Higher Order Function 
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

print("=" * 50)

# With Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]   ==>     [1,4,9,16,25]
# map(function, iterable)
# map(function,[1,2,3,4,5])
lambda num:num * num 
map((lambda num:num * num),[1,2,3,4,5])
print(map((lambda num:num * num),[1,2,3,4,5]))
print(list(map((lambda num:num * num),[1,2,3,4,5]))) # One Liner Functions

print("=" * 50)

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Assume In Real World You Have 50k Product Records 
# Requirement: Give Prices After Applying discounts
# Implementing Solution Normal Way i.e Imperative Style (How To Do)

prices_after_discount = []

for product in products:
    print(product)
    price = product['price']
    print("Price Of Product: ",price)
    
    discount = product['discount']
    print("Discount On Product: ",discount)
    
    price_after_discount = price - (price * discount / 100)
    print("Price Of Product After Discount: ",price_after_discount)
    
    # Adding/Storing Discounted Prices 
    prices_after_discount.append(price_after_discount)
    
    print("Prices Of Products After Discount: ",prices_after_discount)

print("=" * 50)

# Assume In Real World You Have 50k Product Records 
# Requirement: Give Prices After Applying discounts
# Implementing Solution Using Higher Order Functions i.e Declarative Style (What To Do)

# print(list(map((lambda num:num * num),[1,2,3,4,5]))) # One Liner Functions
print(list(map((lambda product:product['price'] - product['price'] * product['discount']/100),products))) # One Liner Functions

print("=" * 50)

prices_after_discount = list(map((lambda product:product['price'] - product['price'] * product['discount']/100),products))
print("Prices Of Products After Discount: ",prices_after_discount)
print("=" * 50)

# Without Higher Order Function 
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]

def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

print("=" * 50)

# With Higher Order Function 
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]
# filter(function,Iterable)
# filter(function,[1,2,3,4,5,6,7,8,9,10])
# lambda num:num % 2==0
filter((lambda num:num % 2==0),[1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num:num % 2==0),[1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num:num % 2==0),[1,2,3,4,5,6,7,8,9,10])))

print("=" * 50)

# Real World Use Case Of Working with Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Assume In Real World You Have 50k Product Records 
# Requirement: Find the Premium Products i.e product with price above 25000
# Implementing Solution Normal Way i.e Imperative Style (How To Do)

premium_products = []

for product in products:
    # print(product)
    price = product['price']
    
    if price > 25000:
        print(product)
        premium_products.append(product)
        
    print("Premium Products Collection: ",premium_products)

print("=" * 50)

# Assume In Real World You Have 50k Product Records 
# Requirement: Find the Premium Products i.e product with price above 25000
# Implementing Solution Using Higher Order Functions i.e Declarative Style (What To Do)

# filter(function,Iterable)
# filter(function,[1,2,3,4,5,6,7,8,9,10])
# lambda num:num % 2==0
print(list(filter((lambda product:product['price'] > 25000),products)))

premium_products = list(filter((lambda product:product['price'] > 25000),products))
print("=" * 50)
print("Premium Products Collection: ",premium_products)
print("=" * 50)

# Real World Data Looks and Comes like this in the form of a "file" (csv & xls files) 
# https://e.nodegoat.net/CMS/upload/guide-import_person_spreadsheet_excel.png

