# Branching Structures (Jump Statements) 

for num in range(1,11,1):
    print(num)
    
print("================")

# break - Helps You Exits Loops 
for num in range(1,11,1):
    # Stop The Loop When Num is 5
    if num == 5: # 20k employees, find emp_id(12065), emp found at 12065, stop here 
        break 
    print(num)

print("================")   
    
# continue - Helps You Skip Current Iteration 
for num in range(1,11,1):
    # Skip 5th Iteration
    if num == 5: # 20k employees, find emp_id(12065), emp found at 12065, skip bonus for this new employee
        continue 
    print(num)

print("================")  

# pass: Acts as a Placeholder, Does Nothing 
# Requirement - To Perform Some Operations In The Future 
# When Salary Of An Employee is Above 25000, We Want To Do Something In The Future 

emp_salary = 15000
 
if emp_salary > 25000:
    # We Want To Do Something In The Future 
    pass # park # __________

print("Continue Working With Other Functionalities")

# After 6 Months In Future
# When Salary Of An Employee is Above 25000, We Want To Make Employee Permanent
emp_salary = 35000
if emp_salary > 25000:
    print("Promoted To Permanent Employee")
    
print("================") 

# When Working With OOP, We Have Following Entities  
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 9999999999
    student_gpa = 9.5
    student_enrolled_courses = ["python","ai","cloud"]
    student_courses_prices = (10000,20000,15000)

# Park Below Identities For Future Operations     
class Manager:
    pass
    
class Developer:
    pass 

class Tester:
    pass 