# Dictionary Methods / Operations: What Actions Can Be Done On Dictionaries 

data = {"a":"apple","b":"banana"}
print(data)

# update(): Add / Update Item In Dictionary
data.update({"c":"cherry"}) # If Key Is Not Present, then adds the items
print(data)

data.update({"a":"apricot"}) # If Key Is Present, then updates the items
print(data)

data = {"a":"apple","b":"banana"}
print(data)

# pop(): Remove Item By Key
data.pop("a")
print(data)

# popitem(): Removes Last Item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties Dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): Used To get Value By Key 
data = {"a":"apple","b":"banana"}
print(data)
data.get("a")
print(data.get("a"))
print(data.get("c"))

# keys(): Used To get Keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())

# for key in dict:
    
for key in data.keys():
    print(key)
    
    
# values(): Used To get Values
data = {"a":"apple","b":"banana"}
print(data)
data.values()
print(data.values())

for value in data.values():
    print(value)
    

# items(): Get Item i.e Key & Value Both
data = {"a":"apple","b":"banana"}
print(data)
data.items()
print(data.items())

for item in data.items():
    print(item)
    
# setdefault(): Returns A Value Of Key, If The Key is Already Present
# If Key is not present, then adds the item and then returns the value 
data = {"a":"apple","b":"banana"}
print(data)

data.setdefault("b","blueberry") 
print(data.setdefault("b","blueberry"))

data = {"a":"apple","b":"banana"}
print(data)
print(data.setdefault("c","cherry"))
print(data)

# copy(): Makes Copy 
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)