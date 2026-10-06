# Dictionaries 

# empty dictionary 
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# dict with numeric data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
print(type(data))

# dict with text data 
data = {"course1":"python","course2":"ai","course3":"cloud"}
print(data)

# dict with mixed data 
data = {1:10,2:20,3:30,"course1":"python","course2":"ai","gpa":8.5,"passed":True}
print(data)

# Accessing Data In Dicts 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# First Element 
# first_element = data[0] # KeyError: 0
first_element = data[1] # dict[key]
print(first_element)

# Last Element 
last_element = data[5]
print(last_element)

# unknown_element = data[10] # KeyError: 10
# print(unknown_element)

# Slicing Doesn't Support
# data = {1:10,2:20,3:30,4:40,5:50}
# print(data)
# print(data[1:3:1]) # 20,30
# print(data[0:5:2]) # 10,30,50

# Accessing Individual Elements 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])


# Accessing Individual Elements -> 10k elements
data = {1:10,2:20,3:30,4:40,5:50,1000:100000}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[4])
# print(data[1000])

print("=" * 50)

# Accessing Individual Elements -> 10k elements
data = data = {1:10,2:20,3:30,4:40,5:50,1000:100000}

# Loops
for num in data:
    print(num) # We Get Only Keys 

print("=" * 50)

# Loops - We Get Keys
for key in data:
    print(key) # We Get Only Keys 

print("=" * 50)

# Loops - Now We Want Values dict[key] = value
for key in data:
    print(data[key]) # Get Values i.e dict[key]

print("=" * 50)

# Operators -> Requirement: Multiply Each Number with 10 
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)

print("=" * 50)

# Requirement: Convert Courses To Upper Case
data = {"course1":"python","course2":"ai","course3":"cloud"}
print(data)

for course in data:
    print(data[course].upper())
    
print("=" * 50)

# Conditionals -> Requirement: Get Only Even Numbers
data = {1:10,2:20,3:35,4:40,5:55}
print(data)
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
print("=" * 50)

# Duplicates Values Allowed
data = {1:10,2:20,3:10,4:40,5:10}
print(data)


# Duplicates Keys -> If We Add Duplicate Key, Latest Key Will Override Old Key 
data = {1:10,2:20,1:30,4:40,5:50}
print(data)

# Values Can Be Any Kind Of Objects 
data = {1:10,2:20,3:30,"course1":"python","course2":"ai","gpa":8.5,"passed":True}

# Keys Can Be Only Immutable Objects 
data = {"course1":"python","course2":"ai","course3":"cloud"}
print(data)

# Keys Can Be Only Immutable Objects 
# data = {['course1']:"python",['course2']:"ai"} # TypeError: unhashable type: 'list'
# print(data)

data = {('course1'):"python",('course2'):"ai"}
print(data)

# Mutable / Immutable -> Dictionaries Are Mutable
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
data[1] = 100
print(data)
# print(dir(data))

# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

