# File Management With Python 

# Syntax - 1

# file = open("file.txt","r")  

file_data = open("14_file_manage/file.txt","r") 
print(file_data)
print(file_data.read())
print(file_data.closed) # False --> Still Open 
file_data.close()
print(file_data.closed) # True --> Now File Is Closed

print("=" * 50)

# Syntax - 2 (Recommended)
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data) 
    print(file_data.read())
print(file_data.closed) # True --> Now File Is Closed

print("=" * 50)

# Create File 
with open("14_file_manage/write.txt","w") as file_data:
    print("File Created") 
    
print("=" * 50)


# Write Data To File 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("File Created Using Python")
    
print("=" * 50)

# Read Data From File 
with open("14_file_manage/write.txt","r") as file_data:
    print(file_data.read())
    
print("=" * 50)

# Delete File 
print("Deleting File")
import os
os.remove("14_file_manage/write.txt") # NameError: name 'os' is not defined. Did you forget to import 'os'?
print("=" * 50)