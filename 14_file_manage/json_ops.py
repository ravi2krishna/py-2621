# Working With JSON Files / Data 

import json

student = {
    "id":101,
    "name": "Ravi",
    "courses": ["python","ai","devops"],
    "gpa": 9.3
}

print(type(student))
print(student)

print("=" * 50)

# Create JSON File and Write Data 
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)
    
print("=" * 50)

# Create JSON File and Write Data With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
print("=" * 50)


# Read JSON File 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    
print("=" * 50)

# From Given JSON File, Read Student Name and Courses He Enrolled
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
print("Student Name: ",data['name'])    
print("Student Enrolled Courses: ",data['courses']) 
print("=" * 50)