# OOP - Object Oriented Programming 

# Class - Blue Print 

class Student:
    
    # Object "HAS" Something like Characteristics / Properties (Variables)
    # Student Has - Name, Email, Gender, Course etc 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    def student_studies():
        print("Student Is Studying Python")
       
# This is function, as it's outside the class 
# def student_studies():
#     print("Student Is Studying Python")
    
# To use this class, we need an object 
student_object = Student()

# print("Student Name: ",student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ",student_email) # NameError: name 'student_email' is not defined

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Object "HAS" Something like Characteristics / Properties (Variables)
    # Student Has - Name, Email, Gender, Course etc 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    def student_studies(self):
        print("Student Is Studying Python")
        
       
# This is function, as it's outside the class 
# def student_studies():
#     print("Student Is Studying Python")
    
# To use this class, we need an object 
student_object = Student()

# print("Student Name: ",student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ",student_email) # NameError: name 'student_email' is not defined

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

student_object.student_studies() 

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Object "HAS" Something like Characteristics / Properties (Variables)
    # Student Has - Name, Email, Gender, Course etc 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended 
        print("Student Email: ",student_object.student_email) # Not Recommended 
    
# To use this class, we need an object 
student_object = Student()

student_object.student_studies() 

print("=" * 50)

# Working With Multiple Objects 
# Class - Blue Print 
class Student:
    
    # Object "HAS" Something like Characteristics / Properties (Variables)
    # Student Has - Name, Email, Gender, Course etc 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended 
        print("Student Email: ",self.student_email) # Recommended 
    
# To use this class, we need an object 
student_ravi = Student()
student_ravi.student_studies() 

student_john = Student()
student_john.student_studies() 

student_mike = Student()
student_mike.student_studies() 

print("=" * 50)

# Working With Multiple Objects 
# Class - Blue Print 
class Student:
    
    # Object "HAS" Something like Characteristics / Properties (Variables)
    # Student Has - Name, Email, Gender, Course etc 
    # student_name = "Ravi"
    # student_email = "ravi@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Call")
        self.student_name = student_name
        self.student_email = student_email
    
    # Object "DOES" Something like Behaviors / Actions (Methods)
    # Student Does - Studies, Attends, Takes Exams etc 
    # self is object reference
    def student_studies(self):
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended 
        print("Student Email: ",self.student_email) # Recommended 
    
# To use this class, we need an object 
# student_ravi = Student() # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
student_ravi = Student("Ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("John","john@gmail.com")
student_john.student_studies() 

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies() 

print("=" * 50)