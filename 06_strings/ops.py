# String Methods 

greet = "hi"
print(greet)
# print(dir(greet))

print("=" * 50)

# capitalize(): Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.
greet = "hi"
result = greet.capitalize()
print(greet)
print(result)

# Above Is Example For Manipulation 

# String Methods For Manipulation, Transformation and Validation.

# Simulate Gmail Functionality - Transformation
#         RAvi2KrIShnA -> ravi2krishna@gmail.com 

email = input("Enter Email ID: ")
print("Original Email Given: "+email)

# lower(): Converts String To Lowercase
transformed_email = email.lower()
print("Transformed Email: "+transformed_email)

# strip(): Remove Spaces From Both Sides
# lstrip(): Remove Spaces From Left Sides
# rstrip(): Remove Spaces From Right Sides

transformed_email = transformed_email.strip()
print("Transformed Email: "+transformed_email)

# add domain @gmail.com 
domain = "@gmail.com"
transformed_email = transformed_email + domain

print("Final Transformed Email: "+transformed_email)

print("=" * 50)

# Simulate PAN CARD Functionality - Validation
# https://www.pan.utiitsl.com//PANform/forms/csf/preCSF

PAN = input("Enter PAN ID: ")
print("Original PAN Given: "+PAN) # @anomp9912w --> anomp9912w --> an12

# isalnum(): returns True if all characters in the string are alphanumeric (letters or numbers)
valid_PAN = PAN.isalnum()
print(f"Given PAN {PAN} is {valid_PAN}")

valid_PAN = PAN.isalnum() and len(PAN) == 10
print(f"Given PAN {PAN} is {valid_PAN}")

if PAN.isalnum() and len(PAN) == 10:
    print("Original PAN: "+PAN)
    # upper(): To convert a string to uppercase in Python
    print("Transformed PAN: "+PAN.upper())
else:
    print(f"Given PAN {PAN} is INVALID")

# 12omp9912w
# First Five Characters Should Be Alphabets
# Next Four Characters Should Be Digits 
# Last Character Should Be Alphabet
    
print("=" * 50)

PAN = input("Enter PAN ID: ")
print("Original PAN Given: "+PAN) # @anomp9912w --> anomp9912w --> an12

if len(PAN) == 10:
    first_five = PAN[0:5:1] # First Five 
    middle_four = PAN[5:9:1] # Next Four
    last_one = PAN[-1] # Last One 
    
    # isalpha(): check if a string is purely alphabetic or not 
    # isdigit(): check if a string is purely digits or not 
    if first_five.isalpha() and middle_four.isdigit() and last_one.isalpha():
        print("Transformed PAN: "+PAN.upper())
    else:
        print(f"Given PAN {PAN} is INVALID")
else:
    print("PAN Should Be 10 Characters Only")
    
# Verify PAN CARD
# Verify AADHAR CARD 
# VERIFY GST NUMBER 

# connect To DB 

# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="your_user",
#     password="your_password",
#     database="your_database",
# )

# pan_id = "ABCDE1234F"

# try:
#     with conn.cursor() as cursor:
#         cursor.execute(
#             "SELECT 1 FROM your_table WHERE PAN_ID = %s LIMIT 1",
#             (pan_id,),
#         )
#         exists = cursor.fetchone() is not None

#     print("Record exists" if exists else "Record does not exist")
# finally:
#     conn.close()
     