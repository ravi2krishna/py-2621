# List Methods / Operations: What Actions Can Be Done On Lists 

# append(): Add Element To End Of The List 
data = [10,20,30,40,50]
print(data)
# data.append() # TypeError: list.append() takes exactly one argument (0 given)
data.append(60)
print(data)

# extend(): Adds Iterable To List 
data = [10,20,30,40,50]
print(data)
# data.extend(60) # TypeError: 'int' object is not iterable
data.extend([60,70,80])
print(data)

# insert(): Add Element On Specific Position i.e Using index 
data = [10,20,40,50]
print(data)
# data.append(30)
# data.insert(30) # TypeError: insert expected 2 arguments, got 1
data.insert(2,30)
print(data)

# pop(): Removes Element By Default Last Element i.e based on index
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data = [10,20,30,40,50]
print(data)
data.pop(2)
print(data)

# remove(): Removes Element By Value 
data = [10,20,30,40,50]
print(data)
data.remove(10)
# data.remove(100) # ValueError: list.remove(x): x not in list
print(data)

data = [10,20,10,30,40,10,50,10]
print(data)
data.remove(10) 
print(data)

# Remove All 10's
data = [10,20,10,30,40,10,50,10]
print(data)
# data.remove(10) 
for x in data:
    if x == 10:
        data.remove(x)
print(data)

# Remove All 10's
data = [10,20,10,30,40,10,50,10]
print(data)
while 10 in data:
    data.remove(10)
print(data)  

# clear(): Empties The List 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): Used To Get The Index Position Of Value
data = [10,20,30,40,50]
print(data)
data.index(20)
print(data.index(20))
# print(data.index(200)) # ValueError: 200 is not in list

# count(): Used To Get Count Of Occurrences 
data = [10,20,10,30,40,10,50,10]
print(data)
data.count(10)
print(data.count(10))

# reverse(): Reverses List 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): Sorts List 
data = [10,30,20,40,50]
print(data)
data.sort() # Default is Ascending Order 
print(data)

data = [10,30,20,40,50]
print(data)
data.sort(reverse=True) # Descending Order 
print(data)

# copy(): Makes Copy Of List 
data = [10,20,30,40,50]
print(data)
backup = data.copy()
print(backup)

# Employee PAN ID's 
pan = ["AAAAA1234A","AAAAA1234B","AAAAA1234C","AAAAA1234D","AAAAA1234D","AAAAA1234D"]
pan[0]
print(pan[0])
# Trying To Change PAN ID 
pan[0] = "AAAAA1234Z"
print(pan[0])

