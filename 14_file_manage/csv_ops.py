# Working With CSV Files

# Read Data From File 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read())
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read().find("Hyderabad"))
    
print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
import csv
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == 'Hyderabad':
            print(row)

print("=" * 50)

# Writing Data To CSV File
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Ramu', 'ramu661@tcs.com', '9833214959', 'Bangalore'])
    csv_writer.writerow(['Kiran', 'kiran645@infosys.com', '9511816384', 'Kolkata'])
    csv_writer.writerow(['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'])

print("=" * 50)
