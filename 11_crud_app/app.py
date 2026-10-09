# Student Management System

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
students = {}

# Build Menu System For CRUD Operations 
while True:
    print("=" * 30)
    print("     Choose An Option: ")
    print("=" * 30)

    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create Student 
        print("=" * 30)
        print("     Creating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ") # 101
        
        if student_id in students:
            print(f"OOPS!!! Student ID {student_id} Already Exists")
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
                    
        
    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)  

    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)   

    elif choice == "4":
        # Read Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30) 
        
    elif choice == "5":
        # Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30) 
        break
        
    else:
        # Invalid Choice
        print("=" * 30)
        print("     Invalid Option, Please Select Only (1-5)")
        print("=" * 30) 