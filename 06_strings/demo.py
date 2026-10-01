# Strings 

# Single Line Strings
s1 = 'hello' # Recommended
print(s1)
print(type(s1))

s1 = "hello" # Recommended
print(s1)
print(type(s1))


s1 = '''hello''' # Not Recommended
print(s1)
print(type(s1))

s1 = """hello""" # Not Recommended
print(s1)
print(type(s1))

# Multi Line Strings

# define_python = 'Python is a high-level, general-purpose programming language 
#         that emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, an extensive ("batteries-included") 
#         standard library, and garbage collection.'

define_python = '''Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection.'''
        
print(define_python)
print(type(define_python))

define_python = """Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection."""
        
print(define_python)
print(type(define_python))

# When you use single quote in a string, enclose them in double quotes 
question = "how are you ?"
# answer = 'i'm fine' # i'm fine
answer = "i'm fine "# i'm fine
print(answer)

# When you use double quote in a string, enclose them in single quotes 
question = "how are you ?"
# answer = "i"m fine "# i"m fine
answer = 'i"m fine'# i"m fine
print(answer)

# When you use both single quote and double quote in a string, 
# enclose them in triple single / double quotes 

question = "how are you ?"
# answer = 'i"m fine 'm fine'
answer = '''i"m fine i'm fine'''
answer = """i"m fine i'm fine"""
print(answer)

# Accessing Strings 
text = "python"
print(text[0])
print(text[1])

print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# Slicing
text = "python"
# len(): Gives Length Of Object 
print(len(text))
print(text[:])
print(text[0:3:1]) # pyt
print(text[1:3]) # yt
print(text[0:5:2]) # pt


                # 0   1 2  3  4  5
                # p   y t  h  o  n
                # -6 -5 -4 -3 -2 -1   

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty

# String Concatenation 
s1 = "Good "
s2 = "Morning"
print(s1+s2)

# Formatted String Literals (f-strings)
age = 30
# print("My Age Is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age Is {age}")

# String Repetition
laugh = "HaHa"
print(laugh)

hard_laugh = laugh * 5
print(hard_laugh)

# String Immutability 
greet = "hi"
print(greet)

# Requirement is Print Hi 
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
# print(greet[0])

print("=" * 30)

# Example For Mutable Data Type i.e List 
greet = ['h','i']
print(greet[0])
greet[0] = "H"
print(greet[0])

