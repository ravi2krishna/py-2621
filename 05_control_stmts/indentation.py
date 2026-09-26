# Indentation Rules

# -> When to use Space -> When We Write Block Of Code
# -> When Not to use Space -> Single Statement 
# -> How many spaces to use -> At least one space, Python Recommended is 4 Spaces (tab)

print("Good Morning") # When Not to use Space -> Single Statement 

#  print("Good Morning") # IndentationError: unexpected indent
#    print("Good Morning") # IndentationError: unexpected indent

# -> When to use Space -> When We Write Block Of Code
# class Student: # IndentationError: expected an indented block after class definition on line 13
# student_name = "Ravi"

# At least One Space
class Student: 
 student_name = "Ravi"

# two spaces
class Student: 
  student_name = "Ravi"
  
# ten spaces
class Student: 
          student_name = "Ravi"
          
# Python Recommended is 4 Spaces (tab)
class Student:
    student_name = "Ravi"

# Consistent Number Of Spaces 
# class Student:
#     student_name = "Ravi" # 4 spaces 
#  student_email = "ravi2krishna@gmail.com" # 1 spaces # IndentationError: unindent does not match any outer indentation level
 
class Student:
    student_name = "Ravi" # 4 spaces 
    student_email = "ravi2krishna@gmail.com" # 4 spaces
 