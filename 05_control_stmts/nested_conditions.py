# Nested Conditionals 

# inner condition is only checked if the outer condition is true

if True:
    print("One")
if True:
    print("This is NOT Nested Condition")
    
if True: # Outer Condition
    print("1")
    if True: # Inner Condition
        print("This IS Nested Condition")
        
if False: # Outer Condition
    print("1")
    if True: # Inner Condition
        print("This IS Nested Condition")
        
# Nested Condition Use Case 
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID Proof")           
else:
    print("You Cannot Vote With Under Age")
    
# Real World Use case 
# Multi Factor Authentication
# Net Baking Login -> SBI -> User Authentication (username & password) -> Prompts For Authorization(OTP)

# Task: Create Multi Factor Authentication

