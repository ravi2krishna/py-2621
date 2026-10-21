# External Modules 

# API - https://dummyjson.com/products

# Check API and Process 

# response = requests.get('https://dummyjson.com/products') # NameError: name 'requests' is not defined

import requests # ModuleNotFoundError: No module named 'requests'
response = requests.get('https://dummyjson.com/products') 

# pip install requests (run this is terminal)

import requests # ModuleNotFoundError: No module named 'requests'
response = requests.get('https://dummyjson.com/products') 
status_code = response.status_code
print(status_code)

print("=" * 50)

response = requests.get('https://dummyjson.com/users') 
status_code = response.status_code
print(status_code)

print("=" * 50)

response = requests.get('https://dummyjson.com/users') 
status_code = response.status_code
print(status_code)

print("=" * 50)

response = requests.get('https://dummyjson.com/countries') 
status_code = response.status_code
print(status_code)

print("=" * 50)


response = requests.get('https://dummyjson.com/countries') 
status_code = response.status_code
if status_code == 200:
    print("Processing API")
else:
    print("Processing API Failed")

print("=" * 50)

response = requests.get('https://dummyjson.com/users') 
status_code = response.status_code
if status_code == 200:
    print("Processing API")
else:
    print("Processing API Failed")

print("=" * 50)