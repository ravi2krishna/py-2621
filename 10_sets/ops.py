# Set Methods / Operations: What Actions Can Be Done On Sets 

# add(): Add Element To Sets 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): Add Multiple Elements To Sets 
data = {10,20,30,40,50}
print(data)
data.update([60,70,80,90])
print(data)

# pop(): Remove Element Randomly
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Remove Element By Value 
data = {10,20,30,40,50}
print(data)
data.remove(30)
# data.remove(100) # KeyError: 100
print(data)

# discard(): Remove Element By Value 
data = {10,20,30,40,50}
print(data)
data.discard(30)
data.discard(100) 
print(data)

# clear(): Empties Set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Create Copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# Special Methods Specific To Sets Only 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combine Sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): Get Common Elements From Sets
print(s1.intersection(s2))
print(s1 & s2)

print(s1)
print(s2)

# intersection_update(): Get Common Elements From Sets, Updates Calling Set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.intersection_update(s2))

print(s1)
print(s2)

# NOTE: Moving forward all _update() methods does the same

# difference(): Removes Common Elements From Set and Gives Unique Elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference(s2))
# print(s2.difference(s1))

print(s2 - s1)

print(s1)
print(s2)

# difference_update(): Removes Common Elements From Set and Gives Unique Elements, Updates Calling Set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference_update(s2))

print(s1)
print(s2)

# symmetric_difference(): Removes Common Elements From Set and Gives Combined Elements From Sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference(s2))

print(s1 ^ s2)

print(s1)
print(s2)


# symmetric_difference_update(): Removes Common Elements From Set and Gives Combined Elements From Sets, Updates Calling Set   
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference_update(s2))

print(s1)
print(s2)

# issubset(): Checks If Given Set Is Subset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): Checks If Given Set Is Superset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issuperset(s1))
print(s1.issuperset(s3))

# isdisjoint(): Checks If Given Set have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.isdisjoint(s3))
print(s1.isdisjoint(s2))
print(s3.isdisjoint(s2))
