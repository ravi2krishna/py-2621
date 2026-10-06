# Tuple Methods / Operations: What Actions Can Be Done On Tuples 

# index(): Used To Get The Index Position Of Value
data = (10,20,30,40,50)
print(data)
data.index(20)
print(data.index(20))
# print(data.index(200)) # ValueError: 200 is not in list

# count(): Used To Get Count Of Occurrences 
data = (10,20,10,30,40,10,50,10)
print(data)
data.count(10)
print(data.count(10))

# Employee PAN ID's -> List 
pan = ["AAAAA1234A","AAAAA1234B","AAAAA1234C","AAAAA1234D","AAAAA1234D","AAAAA1234D"]
pan[0]
print(pan[0])
# Trying To Change PAN ID 
pan[0] = "AAAAA1234Z"
print(pan[0])

print("=" * 50)

# Employee PAN ID's -> Tuples 
pan = ("AAAAA1234A","AAAAA1234B","AAAAA1234C","AAAAA1234D","AAAAA1234D","AAAAA1234D")
pan[0]
print(pan[0])
# Trying To Change PAN ID 
pan[0] = "AAAAA1234Z" # TypeError: 'tuple' object does not support item assignment
print(pan[0])

