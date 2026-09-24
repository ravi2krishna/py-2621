# Data Types 

# Numeric Types 

data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

# data = a + ib
# data = 5 + i3
# data = a + bj # Python format
data = 5 + 3j
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None
print(type(data))

data = "python"
print(type(data))

# Lists 
data = [10,20,30,40,50]
print(type(data))

# Tuples 
data = (10,20,30,40,50)
print(type(data))

# Sets 
data = {10,20,30,40,50}
print(type(data))


# Dictionaries 
data = {"course":"python","time":9,"duration":60}
print(type(data))

# Custom Data Type To Hold Students Data 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 9999999999
    student_gpa = 9.5
    student_enrolled_courses = ["python","ai","cloud"]
    student_courses_prices = (10000,20000,15000)
    
data = Student()
print(type(data))

# Type Conversion / Implicit Conversion (Automatic)
n1 = 10  # int
n2 = 5.5 # float 
sum = n1 + n2 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion (Manually Done By Developer)
price = 1199.20 # float 
print(price)
print(type(price))

# Round Off Price 
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))

# How Casting Is Needed In Real World Applications 
# Some USer In A Web Site Is Filling Some Form (Text Boxes) -> Behind The Scenes They Are Strings 
rating = "2"
print(type(rating))

# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
print(type(rating))
if rating >= 4:
    print("Positive Feedback")
else:
    print("Negative Feedback")
    
    