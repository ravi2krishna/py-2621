# Working With CSV Files

# Read Data From File 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read())
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read().find("Hyderabad"))
    
print("=" * 50)