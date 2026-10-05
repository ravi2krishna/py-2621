# Lists 

# empty list 
empty_list = []
print(type(empty_list))
print(empty_list)

empty_list = list()
print(type(empty_list))
print(empty_list)

# list with numeric data 
data = [10,20,30,40,50]
print(data)

# list with text data 
data = ["python","ai","cloud"]
print(data)

# list with mixed data 
data = [10,20,30,"python","ai",5.5,True]
print(data)

# Accessing Data In Lists 
data = [10,20,30,40,50]
print(data)

# First Element 
first_element = data[0]
print(first_element)

# Last Element 
last_element = data[-1]
print(last_element)

# unknown_element = data[10] # IndexError: list index out of range
# print(unknown_element)

# Slicing 
data = [10,20,30,40,50]
print(data)
print(data[1:3:1]) # 20,30
print(data[0:5:2]) # 10,30,50

# Accessing Individual Elements 
data = [10,20,30,40,50]
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Accessing Individual Elements -> 10k elements
data = [10,20,30,40,50,60,10000]
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])

print("=" * 50)

# Accessing Individual Elements -> 10k elements
data = [10,20,30,40,50,60,10000]

# Loops
for num in data:
    print(num)

print("=" * 50)

# Operators -> Requirement: Multiply Each Number with 10 
data = [10,20,30,40,50]
for num in data:
    print(num * 10)

print("=" * 50)

# Requirement: Convert Courses To Upper Case
data = ["python","ai","cloud"]
print(data)
for course in data:
    print(course.upper())
    
print("=" * 50)

# Conditionals -> Requirement: Get Only Even Numbers
data = [10,20,35,40,55] 
print(data)
for num in data:
    if num % 2 == 0:
        print(num)
print("=" * 50)

# Duplicates Allowed 
data = [10,20,10,30,40,10,50,10]
print(data)

# Insertion Order Preserved 
data = [10,20,30,40,50]
print(data)

# List Operations / Methods 
data = [10,20,30,40,50]
print(dir(data))