# Operators

# Arithmetic Operators 

num1 = 10
num2 = 5

print("Sum of Numbers: ", num1 + num2)
print("Difference of Numbers: ", num1 - num2)
print("Product of Numbers: ", num1 * num2)
print("Division of Numbers: ", num1 / num2)
print("Modulus of Numbers: ", num1 % num2)

print("Normal Division: ", 3/2) # 1.5 

print("Floor Division: ", 3//2) # 1

print("Exponentiation: ", 3 ** 2) # 3 ^ 2

print("============================")

# Compound Assignment Operators 

num = 10
num = num + 5 # Long Form
print(num)

num = 10
num += 5 # Short Form
print(num)

# Increment and Decrement Operators 
count = 10001
print(count)
# count++ # SyntaxError: invalid syntax
count += 1 # count++
print(count)

count += 1 
print(count)

count += 1 
print(count)

count = 10
print(count)

count -= 1 
print(count)

count -= 1 
print(count)

print("============================")

# Comparison Operators 
num1 = 3
num2 = 2
print(num1 > num2)
print(num1 < num2)
print(num1 != num2)

print("============================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1 

print(num1 > num2 and num3 < num1) # T and T = T
print(num1 > num2 and num3 < num4) # T and F = F

print(num1 > num2 or num3 < num4) # T or F = T

print(num1 > num2) # T
print(not num1 > num2) # T

print("============================")

# Membership Operators 
data = "python is programming language"
find_word = "java"
status = find_word in data
print(status)

emp_ids = [101,102,103,105,109,110,120,150] 
find_emp = 109
status = find_emp in emp_ids
print(status)

find_emp = 100
status = find_emp not in emp_ids
print(status)

print("============================")

# Identity Operators 
value_x = 10
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10
print(id(value_z))

print(value_x is value_y)
print(value_x is value_z)
print(value_x is not value_y)

print("============================")

# Bitwise Operators
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000001
       # 0000000000000111
       
print(n1 | n2)
print(n1 & n2)


