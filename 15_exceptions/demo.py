# Exception Handling 

# When No Errors -> Nothing To Handle 

print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ",num1/num2)

print("Program Execution Completed")

print("=" * 50)

# When Errors Occurs -> Program Stopped 

print("Program Execution Started")

num1 = 10
num2 = "5"

# print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

print("Program Execution Completed")

print("=" * 50)

# When Errors Occurs -> We Want To Handle Exceptions

print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING!!! Don't Divide Numeric Values With Strings/Text")

print("Program Execution Completed")

print("=" * 50)

# When Errors Occurs -> We Want To Handle Exceptions

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING!!! Don't Divide Numeric Values With Strings/Text")

print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 0

# print("Result: ",num1/num2) # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50) 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50) 

# When We Come Across Multiple Errors 

print("Program Execution Started")

# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data:
    print(1/num) # 1/1 - 1/2 - 1/'three' - 1/0 - 1/4
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50) 

# When We Come Across Multiple Errors 

print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/'three' - 1/0 - 1/4
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        print("OOPS!!!! Something Went Wrong")

print("Program Execution Completed")

print("=" * 50) 

# When We Come Across Multiple Errors 

print("Program Execution Started")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/'three' - 1/0 - 1/4
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS!!!! Don't Divide Numeric Values With Strings/Text")
    except ZeroDivisionError:
        print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
        
print("Program Execution Completed")

print("=" * 50) 

# else - when there is no error execute this code block 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
    
print("Program Execution Completed")

print("=" * 50) 

# else - when there is no error execute this code block 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # Verify Login Credentials
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check For OTP
    
print("Program Execution Completed")

print("=" * 50) 

# finally - Runs This Block Of Code whether an exception raised or not 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ",num1/num2) # Verify Login Credentials
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check For OTP
finally:
    print("Closing All Opened File Streams and Database Connections")

print("Program Execution Completed")

print("=" * 50) 

# finally - Runs This Block Of Code whether an exception raised or not 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ",num1/num2) # Verify Login Credentials
except:
    print("OOPS!!!! Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check For OTP
finally:
    print("Closing All Opened File Streams and Database Connections")

print("Program Execution Completed")

print("=" * 50) 

# Without User Defined Exceptions and raise keyword

print("Program Execution Started")

age = int(input("Enter Your Age: "))

if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
print("Program Execution Completed")

print("=" * 50) 

# With User Defined Exceptions and raise keyword

class UnderAgeError(Exception):
    pass 

print("Program Execution Started")

age = int(input("Enter Your Age: "))

if age < 18:
    # raise TypeError # Unrelated Error 
    # raise UnderAgeError
    raise UnderAgeError("Below 18 Are Not Allowed To Vote")
else:
    print("You Can Vote")
    
print("Program Execution Completed")

print("=" * 50) 