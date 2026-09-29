# Looping Structures (Iteration Statements) (Repetition)

# while loop 

while False:
    print("Repeat...")
    print("Code............")
    
# while True: # This forms infinite loop 
#     print("Repeat...")
#     print("Code............") 

# To Stop Above infinite loop press  control + c 

# Counters 
count = 1
while count <= 5:
    print("Count Is: ",count)
    count += 1 
    
print("=====================")

# Requirement: Generate Employee ID's 10001 - 15000
emp_id = 10001
while emp_id <= 15000:
    print("Employee ID Generated: ",emp_id)
    emp_id += 1
    
print("=====================")

# We Use while loop, when we don't know 
# Number Of Iterations / Repetitions In Advance.

# You Found A Lost Phone, Trying To Break PIN / Password 
# Tell Me At Which Attempt, The Phone Will Be Unlocked ?

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN To Unlock: ")
print("Phone Unlocked")

print("=====================")

# for loop 
prices_products = [1000,1500,2000,2500,100000]

# Requirement: Some Offer is running -> Provide a discount of 250 on each product 
# In Lists We Have Index, which starts from Zero and Keeps Increasing 
# Without for loop
print("======== Prices Before Discount ========")
print(prices_products[0])
print(prices_products[1])
print(prices_products[2])
print(prices_products[3])
print(prices_products[4])
# print(prices_products[5])
# print(prices_products[.])
# print(prices_products[.])


print("======== Prices After Discount ========")
print(prices_products[0] - 250)
print(prices_products[1] - 250)
print(prices_products[2] - 250)
print(prices_products[3] - 250)
print(prices_products[4] - 250)
# print(prices_products[5] - 250)
# print(prices_products[.] - 250)
# print(prices_products[.] - 250)

# With for loop
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
print("======== Prices Before Discount ========")
for price in prices_products:
    print("Price of Product Before Discount: ",price)

print("======== Prices After Discount ========")
for price in prices_products:
    print("Price of Product After Discount: ",price - 250)
    
print("=====================")

# range() function
# range(start, stop, step) 

for num in range(6): # range(0,6,1)
    print(num)
    
print("=====================")

for num in range(0,11,1):
    print(num)
        
print("=====================")

for emp_id in range(10001,15001,1):
    print("Employee ID Generated: ",emp_id)
        
print("=====================")

# prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,100000]
for price_product in range(1000,100500,500):
    print("Price of Product: ",price_product)
        
print("=====================")


for num in range(1,11,1):
    print(num)

print("=====================")  

for num in range(10,0,-1):
    print(num)