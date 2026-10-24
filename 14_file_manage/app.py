# Student Management System -> Using Functional Approach -> Use Persistent Storage i.e Save Data To File

# Menu Based System -> In Future When You Learn Frontend(HTML/CSS/JS), 
# Replace Menus With UI Elements Like Buttons 

# System Info -> READ ONLY (Tuple)
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")


# Admin Info -> READ ONLY (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)

print(f"            Welcome To {SYSTEM_INFO[0]}")
print(f"    Software Name Is {SYSTEM_INFO[1]} - {SYSTEM_INFO[-1]}")

print("=" * 50)

# Implement Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores & SKills 
# Student Data Representation

# students = {
#     "101":{
#         "name": "Ravi",
#         "scores": [90,80,80,70],
#         "skills": {"python","ai"}
#     },
#     "102":{
#         "name": "John",
#         "scores": [90,80],
#         "skills": {"java","sql"}
#     }
# }

# students dictionary is where we will store students data
# students = {}

# Importing Utilities 
import json,os 

# File To Store Students Data 
FILE_NAME = "14_file_manage/students.json"

# Load Students Data JSON File 
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file_data:
            return json.load(file_data)
    else:
        return {}

# Set Student Details
students = load_students()
    
# Save Students Data To JSON File 
def save_students():
    
# TypeError: Object of type set is not JSON serializable
        # Fix Above Issue By Converting To List Format
        json_data_fix = {
            # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
            sid: {
                "name": data['name'],
                "scores": data['scores'],
                "skills": list(data['skills'])
            }
            for sid,data in students.items()
        }
        
        with open(FILE_NAME,"w") as file_data:
            json.dump(json_data_fix,file_data,indent=4)
        

# Add Student Function
def add_student():
        # Create Student 
        print("=" * 30)
        print("     Creating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ") # 101
        
        if student_id in students:
            print("=" * 50)
            print(f"OOPS!!! Student ID {student_id} Already Exists")
            print("=" * 50)
            
        else:
            name = input("Enter Name: ").title() # ravi krishna
            # name = name.title()
            
            scores = []
            
            while True:
                score_input = input("Enter Score or Type done: ") # 90, 80, 80 done
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print(f"Invalid Score {score_input}, Score Should Be (0-100) Only")
                else:
                    print(f"Invalid Score {score_input}, Score Should Be Digits Only")
                    
            
            skills = set()
            
            while True:
                skill_input = input("Enter Skill or Type done: ") # ai, python, ai done
                if skill_input == "done":
                    break            
                else:
                    skills.add(skill_input)
                    
            
            print(students) # Before Adding 
            
            # Saving Student Using Key
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills                
            }
            
            print("=" * 50)
            print(f"Student ID {student_id} Added Successfully")
            print("=" * 50)
            
            save_students() # Create Student In JSON File 
            print(students) # After Adding 
            
# Update Student Function
def update_student():
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30) 
        
        student_id = input("Enter ID To Update: ") # 101
        
        if student_id in students:
            new_name =  input("Enter New Name: ").title() # ravi krishna
            students[student_id]['name'] = new_name
            
            print("=" * 50)
            print(f"Student ID {student_id} Updated Successfully")
            print("=" * 50)
            
        else:
            print("=" * 50)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exists")
            print("=" * 50)
        
        save_students() # Updating Student In JSON File     
        print(students) # After Updating 

            
# Delete Student Function
def delete_student():
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)  
        
        student_id = input("Enter ID To Delete: ") # 101
        
        if student_id in students:
            
            students.pop(student_id)
            
            print("=" * 50)
            print(f"Student ID {student_id} Deleted Successfully")
            print("=" * 50)
            
        else:
            print("=" * 50)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exists")
            print("=" * 50)
            
        save_students() # Deleting Student In JSON File     
        print(students) # After Deleting  

            
# Read Student Function
def read_student():
        # Read Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30) 
        
        student_id = input("Enter ID To Read: ") # 101
        
        if student_id in students:
            # Fetch Specific Student Data
            # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
            data = students[student_id]
            
            # data = {'name': 'Ravi', 'scores': [90,80], 'skills': {'python','ai'}}
            name = data['name'] # Ravi 
            scores = data['scores'] # 90, 80
            skills = data['skills'] # python, ai
            
            # Average Score 
            total_score = 0 # 90 + 80 
            current_score_count = 0 # 0 + 1 + 1
            
            for score in scores:
                total_score += score 
                current_score_count += 1
            
            average_score = total_score / current_score_count
            
            # Highest Score [90,80,100]
            high_score = scores[0] # 100 
            
            for score in scores: 
                if score > high_score: # 100 > 90 
                    high_score = score
                    
            
            # Lowest Score [90,80,100]
            low_score = scores[0] # 90
            
            for score in scores:
                if score < low_score:
                    low_score = score  
            
            # Skills Count 
            skill_count = 0
            
            for skill in skills:
                skill_count += 1 
                
            print("=" * 50)           
            print(f"    Reading Student {student_id} Details")
            print("=" * 50)           
            
            print(f"Student ID: {student_id}")
            print(f"Student Name: {name}")
            print(f"All Scores: {scores}")
            print(f"Average Score: {average_score}")
            print(f"Highest Score: {high_score}")
            print(f"Lowest Score: {low_score}")
            print(f"All Skills: {skills}")
            print(f"Skills Count: {skill_count}")
        
        else:
            print("=" * 50)
            print(f"OOPS!!! Student ID {student_id} Doesn't Exists")
            print("=" * 50)


# Search Student Function
def search_student():
        # Search Student 
        print("=" * 30)
        print("     Searching Student")
        print("=" * 30) 
        
        skill_to_search = input("Enter Skill To Search: ") # python / ai / devops
        # premium_products = list(filter((lambda product:product['price'] > 25000),products))
        filtered_students = list(filter((lambda student_id: skill_to_search in students[student_id]['skills']),students))
        # print(f"Students With Skill {skill_to_search} - {filtered_students}")
        
        if filtered_students:
            print("=" * 50)
            print(f"     Students With Skill {skill_to_search}")
            print("=" * 50) 
            
            for student_id in filtered_students:
                print(f"Student ID {student_id} - Student Name {students[student_id]['name']}")
        
        else:
            print(f"     Students With Skill {skill_to_search} Not Found!!!!")
        

# Exit Application Function
def exit_app():
# Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30) 
        
        # Display Admin Info 
        print("=" * 50)
        print(f"    Admin Contact Number {ADMIN_INFO[0]}")
        print(f"    Admin Email Address {ADMIN_INFO[1]}")
        print("=" * 50)

# Build Menu System For CRUD Operations 
while True:
    print("=" * 30)
    print("     Choose An Option: ")
    print("=" * 30)

    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Search By Skill")
    print("6 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        add_student()
             
    elif choice == "2":
       update_student() 

    elif choice == "3":
        delete_student()

    elif choice == "4":
        read_student()
    
    elif choice == "5":
        search_student()
 
    elif choice == "6":
        exit_app()
        break
        
    else:
        # Invalid Choice
        print("=" * 30)
        print("     Invalid Option, Please Select Only (1-6)")
        print("=" * 30) 