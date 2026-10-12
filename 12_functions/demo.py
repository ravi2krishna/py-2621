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